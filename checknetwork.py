#!/usr/bin/env python3

import pprint
import subprocess
import statistics

# Import library and create instance of REST client.
#from Adafruit_IO import Client, Data
#aio = Client('XXXX')


iproute = subprocess.check_output(['ip', 'route', 'show'])

defrouter = iproute.splitlines()[0].split()[2]

print("Default router is: " + str(defrouter))


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


trace = subprocess.check_output(['traceroute', '-n', '-f 2', '-m 2', '8.8.8.8'])

traceRes = trace.splitlines()
print(traceRes)

# 2  142.254.217.45  16.680 ms  26.592 ms  26.274 ms
print("First result is: " + str(traceRes[1].split()[2]))

print(statistics.mean([float(traceRes[1].split()[2]), \
                       float(traceRes[1].split()[4]), \
                       float(traceRes[1].split()[6]), \
                      ]))

