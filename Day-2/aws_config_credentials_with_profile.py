#!/usr/bin/python
import boto3,time,pprint
root_session=boto3.session.Session(profile_name="default")
ec2_con_re=root_session.resource('ec2',"us-east-1")
ec2_con_cli=root_session.client('ec2','us-east-1')
'''
re_cnt=1
print "=====================Below output is using resource method==========================="
for each_re in dir(ec2_con_re):
  print re_cnt,".",each_re
  re_cnt=re_cnt+1
time.sleep(3)
print "=====================Below output is using client method============================="
cli_cnt=1
for each_cli in dir(ec2_con_cli):
  print cli_cnt,".",each_cli
  cli_cnt=cli_cnt+1
'''
'''
for each_instance in ec2_con_re.instances.all():
   print each_instance.id,each_instance.state,each_instance.instance_type,each_instance.key_name
   #print dir(each_instance)
   #break
'''

for each_in in  ec2_con_cli.describe_instances()['Reservations']:
    for instance_details in each_in['Instances']:
        print instance_details
    time.sleep(5)
