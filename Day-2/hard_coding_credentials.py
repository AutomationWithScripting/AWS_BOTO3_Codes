#!/usr/bin/python
import boto3
root_session=boto3.session.Session(aws_access_key_id="XXXXXXXXXX",aws_secret_access_key="XXXXXXXXX")
ec2_con=root_session.resource('ec2',"us-east-1")
print dir(ec2_con)
