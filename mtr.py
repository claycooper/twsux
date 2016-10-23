#!/usr/bin/env python3

import pprint
import subprocess
#import statistics
import json

# Import library and create instance of REST client.
#from Adafruit_IO import Client, Data
#aio = Client('XXXXXX')


# Get list of feeds.
#feeds = aio.feeds()

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(feeds)

#print('+-' * 20)

# Print out the feed names:
#for f in feeds:
#    print('Feed: {0}'.format(f.name))

#feed = raw_input('Feed Name: ')
#newvalue = raw_input('Value: ')

#data = Data(value=defrouter)
#aio.create_data("twc-local-router-ip", data)


# mtr --json -c1 8.8.8.8
trace = subprocess.check_output(['mtr', '--json', '-c1', '142.254.217.45'])
traceStr = str(trace, 'utf-8')

#print(str(trace, 'utf-8'))

traceObj = json.loads(traceStr)
#json.dumps(trace)
print(traceObj['report'])

for hub in traceObj['report']['hubs']:
  print(hub['host'] + "-" + str(hub['Avg']))
#  print(hub)

