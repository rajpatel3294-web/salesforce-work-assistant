# Synthetic support case

All identifiers below are synthetic. No Salesforce or Mule instance is connected.

User report: A Case update sometimes never creates a repair order. Restarting the
Mule app usually restores processing. Yesterday a duplicate repair order appeared.

Observed log excerpts:
2026-10-08T14:00:01Z publisher businessKey=CASE-DEMO-41 eventUuid=event-demo-7 publishAccepted=true
2026-10-08T14:00:02Z subscriber replayCursor=opaque-demo-A received businessKey=CASE-DEMO-41
2026-10-08T14:00:03Z outbound requestId=req-demo-9 CreateRepair businessKey=CASE-DEMO-41
2026-10-08T14:00:13Z outbound requestId=req-demo-9 timeout waiting for response
2026-10-08T14:04:00Z app restarted
2026-10-08T14:04:02Z subscriber replayCursor=opaque-demo-B received businessKey=CASE-DEMO-41
2026-10-08T14:04:03Z outbound requestId=req-demo-10 CreateRepair businessKey=CASE-DEMO-41
2026-10-08T14:04:04Z outbound requestId=req-demo-10 success order=ORDER-DEMO-102

Support later sees two orders for CASE-DEMO-41. The original outbound payload,
first target acknowledgement, connector version and Object Store settings are not supplied.

