#!/usr/bin/python
import sys
try:
  import boto3
except Exception as e:
  print e
  sys.exit()

ec2_in=boto3.resource("ec2",'us-east-1')
for each in ec2_in.meta.client.describe_regions()['Regions']:
  print each['RegionName']
