import boto3
import json

s3 = boto3.client('s3')
# Specify your AWS credentials (Access Key ID and Secret Access Key)
# aws_access_key_id = 'aws_access_key_id'
# aws_secret_access_key = 'aws_secret_access_key'

# Create an S3 resource
# s3_resource = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='us-east-1')

# Specify the bucket name you want to create
# new_bucket_name = 'boto3-practice-sp'

# Create the new bucket without specifying a location constraint
# s3_resource.create_bucket(Bucket=new_bucket_name)

#list of bucket 
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(bucket['Name'])

# put_object()- Adds an object to a Bucket

json_object= {"Name":"kaggle","bucket":"demo-bucket-kagglebucket4"}
s3.put_object(
    Body=str(json.dumps(json_object)),
    Bucket='boto3-practice-sp',
    Key='test.json'
)

# upload_file()- upload a file to S3 Bucket
# upload_file(Filename, Bucket, Key)

s3.upload_file('test_upload.json', 'boto3-practice-sp', 'hello.json')

# delete_object()- removes the object from S3 Bucket

#  s3.delete_object(Bucket="boto3-practice-sp", Key="hello.json")

# Another way to delete object that has already been retrieved from s3 Bucket

# s3_del = boto3.resource('s3')
# obj = s3_del.Object('boto3-practice-sp', 'hello.json')
# obj.delete()

#Creates a copy of an object that is already stored in S3 Bucket

try:
    response = s3.copy_object(
        CopySource={'Bucket': 'boto3-practice-sp', 'Key': 'hello.json'},
        Bucket='boto3-practice-sp',
        Key='hello_copy.txt'
    )
    print("Object copied successfully")
except Exception as e:
    print(f"An error occurred: {e}")

