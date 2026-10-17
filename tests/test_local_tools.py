import importlib.util
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/f'{name}.py')
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value

snapshot = module('metadata_snapshot').snapshot
compare = module('compare_snapshots').compare
install = module('install_skills').install

class MetadataTests(unittest.TestCase):
    def test_flow_metadata_and_no_source_body(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'flow.flow-meta.xml').write_text('<Flow xmlns="http://soap.sforce.com/2006/04/metadata"><status>Active</status><triggerOrder>20</triggerOrder><start><object>Case</object><triggerType>RecordAfterSave</triggerType></start></Flow>')
            (root/'Secret.cls').write_text('public class Secret { /* private business logic */ }')
            result = snapshot(root)
            flow = next(x for x in result['files'] if x['path'].endswith('.xml'))
            self.assertEqual('Case', flow['object'])
            self.assertEqual('20', flow['triggerOrder'])
            self.assertNotIn('private business logic', str(result))

    def test_excludes_auth_and_symlinks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'.sf').mkdir()
            (root/'.sf'/'auth.xml').write_text('<auth>secret</auth>')
            (root/'ok.cls').write_text('class Fine {}')
            try:
                (root/'linked.cls').symlink_to(root/'ok.cls')
            except OSError:
                pass
            self.assertEqual(['ok.cls'], [x['path'] for x in snapshot(root)['files']])

    def test_invalid_xml_and_entity_are_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'bad.xml').write_text('<Flow>')
            (root/'entity.xml').write_text('<!DOCTYPE x [<!ENTITY a "value">]><x>&a;</x>')
            result = snapshot(root)
            self.assertEqual(2, len(result['errors']))
            with self.assertRaises(ValueError):
                compare(result, result)

    def test_changes_are_classified(self):
        before = {'schema_version':1,'files':[{'path':'a','sha256':'1'},{'path':'b','sha256':'2'},{'path':'same','sha256':'x'}]}
        after = {'schema_version':1,'files':[{'path':'a','sha256':'3'},{'path':'c','sha256':'4'},{'path':'same','sha256':'x'}]}
        result = compare(before, after)
        self.assertEqual(['a'], result['changed'])
        self.assertEqual(['b'], result['removed'])
        self.assertEqual(['c'], result['added'])
        self.assertEqual(1, result['unchanged_count'])

    def test_duplicate_paths_rejected(self):
        value = {'schema_version':1,'files':[{'path':'a','sha256':'1'},{'path':'a','sha256':'2'}]}
        with self.assertRaises(ValueError):
            compare(value,value)

    def test_missing_source_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                snapshot(Path(tmp)/'missing')

class InstallerTests(unittest.TestCase):
    def test_all_skills_portable_after_selective_install(self):
        # Resolve references from a clean destination, without access to hub files.
        with tempfile.TemporaryDirectory() as tmp:
            for source in (ROOT/'skills').iterdir():
                install(source.name, tmp, True)
                target = Path(tmp)/source.name
                self.assertTrue((target/'references/project-lifecycle.md').is_file())
                for doc in target.rglob('*.md'):
                    for link in re.findall(r'\]\(([^)]+)\)', doc.read_text()):
                        if '://' in link or link.startswith(('#', 'mailto:')):
                            continue
                        resolved = (doc.parent/link.split('#')[0]).resolve()
                        self.assertTrue(resolved.is_relative_to(target), str(doc))
                        self.assertTrue(resolved.exists(), str(resolved))
            router = Path(tmp)/'sf-route-work/assets'
            for name in ('INDEX.md', 'system-overview.md', 'component-catalog.md',
                         'feature-plan.md', 'decision-record.md', 'handover.md'):
                self.assertTrue((router/name).is_file())

    def test_dry_run_apply_and_overwrite_protection(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)/'sf-investigate-issue'
            result = install('sf-investigate-issue',tmp)
            self.assertFalse(result['copied'])
            self.assertFalse(target.exists())
            install('sf-investigate-issue',tmp,True)
            self.assertTrue((target/'references/runtime-contract.md').exists())
            with self.assertRaises(ValueError):
                install('sf-investigate-issue',tmp,True)

    def test_unknown_or_traversal_name_rejected(self):
        with self.assertRaises(ValueError):
            install('../outside','/tmp')

if __name__ == '__main__':
    unittest.main()

