# Issue Summary

![Alt Text](https://private-user-images.githubusercontent.com/24565896/282248924-8ad5fb26-f1be-4871-b51b-6c41e28fbb54.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTQ5OTQzOTEsIm5iZiI6MTcxNDk5NDA5MSwicGF0aCI6Ii8yNDU2NTg5Ni8yODIyNDg5MjQtOGFkNWZiMjYtZjFiZS00ODcxLWI1MWItNmM0MWUyOGZiYjU0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA1MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNTA2VDExMTQ1MVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdhNDE4N2I0MTQ5YjIyMGU5MzY2OTQ3ODZhMjRjMGEyMTQ1N2Y0ZDNjNjFlMzI0MTcxMDQyOGQyYTk1YzlkNDMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.zTO2a6sQxC7LzSAv4djQuVHoPOh9YL_w7WRCiGLjtQs)



## Duration

- **Start Time:** May 5, 2024, 10:00 PM (UTC-5)
- **End Time:** May 6, 2024, 2:00 AM (UTC-5)

## Impact

The login service experienced intermittent outages, with approximately 30% of users unable to log in during peak hours.

## Root Cause

The authentication microservice failed to scale properly due to a misconfigured load balancer.

## Timeline

### Detection Time

- May 5, 2024, 10:30 PM (UTC-5)
- The monitoring system triggered an alert for increased error rates in the authentication service.

### Actions Taken

- Investigated database performance.
- Checked network connectivity between services.
- Assumed database overload as the root cause initially.

### Misleading Paths

Initially suspected a DDoS attack due to the sudden increase in errors.

### Escalation

Incident was escalated to the DevOps team and then to the infrastructure team for further investigation.

### Resolution

The misconfiguration in the load balancer was corrected, and additional instances of the authentication service were spun up to handle the increased load.

## Root Cause and Resolution

### Root Cause

Misconfigured load balancer settings prevented proper distribution of incoming traffic to backend instances of the authentication service.

### Resolution

Load balancer settings were adjusted to evenly distribute traffic among available instances, and additional instances were provisioned to handle the load during peak times.

## Corrective and Preventative Measures

### Improvements/Fixes

- Regular audits of load balancer configurations to ensure proper scaling.
- Enhanced monitoring for load balancer performance metrics.

### Tasks

- Conduct load testing to simulate peak traffic scenarios.
- Implement automated alerts for load balancer misconfigurations.
- Document load balancer scaling procedures for future reference.

By addressing the misconfiguration in the load balancer and implementing preventive measures, we aim to minimize the impact of similar incidents in the future and ensure the reliability of our services during peak usage periods.

