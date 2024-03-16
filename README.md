# aws_data_engineering
This repository is for AWS data engineering task
1. doordash_delivery_data -
This project creats an automated AWS-based solution for processing daily
delivery data from DoorDash. JSON files containing delivery records will be uploaded to an
Amazon S3 bucket. An AWS Lambda function, triggered by the file upload, will filter the
records based on delivery status and save the filtered data to another S3 bucket.
Notifications regarding the processing outcome will be sent via Amazon SNS.
For deployment, we are using CICD with codebuild.


