import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

#This is code for a lambda fucntion that creates a client connection with dynamodb using boto3, connects that client to my table 'Student'
# than creates a resonse item by scanning for all 'SchoolID' values that equal '70465101' from the studentTable connection we mamde earlier.

#This is not natively possible with the 'Query' command, as we would need the individual student IDs since we are using 'StudentID' as the partition key.
# We should probably consider using a different partition key if we plan on storing data like this




def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    studentTable = client.Table('Student')

    # get item by SchoolID

    response = studentTable.scan(
        FilterExpression=Attr('SchoolID').eq(70465101)
    )
    
    items = (response['Items'])
    for item in items:
        print(item)