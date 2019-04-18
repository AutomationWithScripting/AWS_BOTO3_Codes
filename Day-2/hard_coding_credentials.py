#!/usr/bin/python
import boto3
root_session=boto3.session.Session(aws_access_key_id="AKIAITOXLWMUUVVCFMPA",aws_secret_access_key="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")
ec2_con=root_session.resource('ec2',"us-east-1")
print dir(ec2_con)
