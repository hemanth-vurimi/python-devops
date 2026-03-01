# import boto3

# profile_name = "terraform-dev"

# session = boto3.Session(profile_name=profile_name)
# s3 = session.client("s3")

# response = s3.list_buckets()

# for bucket in response["Buckets"]:
#     print(bucket["Name"])

## cehcking s3 bucket is there or not if not create a bucket with unique name##

# import boto3
# import uuid

# profile_name = "terraform-dev"
# session = boto3.Session(profile_name=profile_name)
# s3 = session.client("s3")

# bucket_name = f"my-unique-bucket-{uuid.uuid4()}"
# try:
#     s3.create_bucket(Bucket=bucket_name)
#     print(f"Created bucket: {bucket_name}")
# except Exception as e:
#     print(f"Error creating bucket: {e}")

## EC2 Inventory Using boto3 ##

import boto3

profile_name = "terraform-dev"
session = boto3.Session(profile_name=profile_name)
ec2 = session.client("ec2")

# response = ec2.describe_instances()

# for reservation in response["Reservations"]:
#     for instance in reservation["Instances"]:
#         instance_id = instance["InstanceId"]
#         instance_type = instance["InstanceType"]
#         state = instance["State"]["Name"]
#         print(f"Instance ID: {instance_id}, Type: {instance_type}, State: {state}")

import boto3

profile_name = "terraform-dev"
session = boto3.Session(profile_name=profile_name)

ec2 = session.client("ec2", region_name="us-east-1")

response = ec2.run_instances(
    ImageId="ami-0b6c6ebed2801a5cb",
    InstanceType="t2.micro",
    KeyName="vpc-peering-demo",
    SecurityGroupIds=["sg-085b50e229d00332c"],
    MinCount=1,
    MaxCount=1
)

print(response["Instances"][0]["InstanceId"])




   
