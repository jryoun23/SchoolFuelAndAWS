# CSV -> S3 -> Lambda Function -> DynamoDB

## This file is going to outline the process for transferring CSV data from S3 to DynamoDB.
### *(I am going to assume that the S3 bucket and DynamoDB tables are already set up)*

### **Step 1 Create a lambda function** 
 1. Go to lambda function in the AWS management console (can be done using CLI but I don't know how yet)
 2. Create a new Lambda function and give it permissions to read from s3 and write to dynamoDB (In this case I jsut gave the function full access to S3 and Dynamo because I was unsure of which function I wanted to write first, the Scan function or the put_item function. I understand that this is a seurity risk, but for training purposes this is fine... I think)
 3. Look at the function [bucketToDynamo.py](bucketToDynamo.py) as it will (in order of execution)
  - Create a Session instance for a given region by using boto3.Session() 
  - connect the session to s3 using the resource('s3')
  - create a new dynamoDB client instance 
  - Create a new bucket object linked to whatever bucket you're going to be reading the csv data from. (the nice thing about lambda functions is that you can make it so when a new file is added to an s3 bucket, you can automatically run this process and have the dynamo table ingest it)
  - next we're going to create a response object via the bucket.get(), which returns us an object hierarchy of the s3 bucket described above.
  - to read this response object, we access the Body of the resonse, read(), decode using 'utf-8-sig' (depends on data type, but this will treat the BOM as its signiture instead of a string(this will depend on the csv filetype I assume)), and then splits each line of data (which are the items for us) into its own python list.
  - what we're left with is a 

