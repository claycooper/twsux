#!/usr/bin/env python3

import pprint
import subprocess
import json
import datetime


# mtr --json -c1 8.8.8.8
trace = subprocess.check_output(['mtr', '--json', '-c1', '142.254.217.45'])
traceStr = str(trace, 'utf-8')

#print(str(trace, 'utf-8'))

traceObj = json.loads(traceStr)
#json.dumps(trace)
print(traceObj['report'])

# {'mtr': {'dst': '142.254.217.45', 'tos': '0x0', 'psize': '64', 'bitpattern': '0x00', 'tests': '1', 'src': 'twsux'}, 'hubs': [{'Wrst': 7.42, 'Avg': 7.42, 'Last': 7.42, 'host': 'router1.home.local', 'Best': 7.42, 'count': '1', 'Loss%': 0.0, 'StDev': 0.0, 'Snt': 1}, {'Wrst': 18.07, 'Avg': 18.07, 'Last': 18.07, 'host': '142.254.217.45', 'Best': 18.07, 'count': '2', 'Loss%': 0.0, 'StDev': 0.0, 'Snt': 1}]}


print(datetime.datetime.now())

for hub in traceObj['report']['hubs']:
  print(' '.join([ hub['host'], str(hub['Avg']), str(hub['StDev']), str(hub['Loss%']) ]))

