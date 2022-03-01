import json
import boto3
import csv

#This is a lambda function that utuilizes the boto3 package to initialize a connection to AWS, create an s3 bucket object, 
# read the files from the bucket, and put_item every individual item into the dynamoDB table.

def lambda_handler(event, context):
    region='us-west-1'
    headers = []
    data = []
    try: 
        # get a handle on s3
        session = boto3.Session(region_name=region)
        s3 = session.resource('s3')
        dyndb = boto3.client('dynamodb', region_name=region)
        bucket = s3.Bucket('stubuc') 
        obj = bucket.Object(key='Students.csv') 
        # get the object
        response = obj.get()
        # read the contents of the file
        lines = response['Body'].read().decode('utf-8-sig').splitlines()
 
        firstrecord=True
        csv_reader = csv.reader(lines, delimiter=',', quotechar='"')
        for row in csv_reader:
            if (firstrecord):
                headers = row
                for header in headers:
                    data.append([])
                firstrecord=False
                continue
            StudentID = row[0]
            SchoolID = row[1]
            AlternateID = row[2]
            LastRevised = row[3]
            ShortName = row[4]
            Gender = row[5]
            BirthDate = row[6]
            Ethnicity = row[7]
            Race = row[8]
            ZipCode = row[9]
            HomeroomStaff = row[10]
            StaffEmailDefault = row[11]
            Grade = row[12]
            EnrollDate = row[13]
            EnrollCode = row[14]
            WithdrawalDate = row[15]
            WithdrawalCode = row[16]
            NbrofRetentions = row[17]
            SPED = row[18]
            ELL = row[19]
            Gifted = row[20]
            Sectfof = row[21]
            ParentRelation = row[22]
            
            response = dyndb.put_item(
                TableName='Student',
                Item={
                'StudentID' : {'N': StudentID},
                'SchoolID': {'N': SchoolID},
                'AlternateID': {'N':AlternateID},
                'LastRevised': {'S':LastRevised},
                'ShortName': {'S':ShortName},
                'Gender': {'N':Gender},
                'BirthDate': {'S':BirthDate},
                'Ethnicity': {'N':Ethnicity},
                'Race': {'N':Race},
                'ZipCode': {'S':ZipCode},
                'HomeroomStaff': {'S':HomeroomStaff},
                'StaffEmailDefault': {'S':StaffEmailDefault},
                'Grade': {'S':Grade},
                'EnrollDate': {'S':EnrollDate},
                'EnrollCode': {'S':EnrollCode},
                'WithdrawalDate': {'S':WithdrawalDate},
                'WithdrawalCode': {'S':WithdrawalCode},
                'NbrofRetentions': {'S':NbrofRetentions},
                'SPED': {'S':SPED},
                'ELL': {'S':ELL},
                'Gifted': {'S':Gifted},
                'Sectfof': {'S':Sectfof},
                'ParentRelation': {'S':ParentRelation}
                }
                )
        result = 'Put succeeded:'
    except Exception as err:
        result = format(err)
    return {
            'Body': result
        }
    
