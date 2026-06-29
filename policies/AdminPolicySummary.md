## IAM Policy Summary

The LogiHaul system uses IAM roles following least privilege principles.

### Lambda Execution Role
- SQS: SendMessage, ReceiveMessage
- SNS: Publish
- DynamoDB: PutItem
- CloudWatch Logs: Write logs

### EC2 Role
- S3 access
- Systems Manager access
