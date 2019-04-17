#!/usr/bin/python
import json
from subprocess import *
cmd='aws ec2 describe-regions --region us-east-1 --output json'
sp=Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE)
rt=sp.wait()
out,err=sp.communicate()
if rt==0:
  out_di=json.loads(out)
  for each_region in out_di['Regions']:
     print each_region['RegionName']
else:
  print err
