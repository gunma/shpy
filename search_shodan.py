#!/usr/bin/env python
#
# search_shodan.py
# Search SHODAN and print a list of IPs matching the query
#
# Modified by: Gunma

from shodan import WebAPI
import sys

SHODAN_API_KEY = "2MiDMdjjnjyyK8KRf6qlNNMQV3yhmizF"

api = WebAPI(SHODAN_API_KEY)

print	""
print	"  _________.__   __________       " 
print	" /   _____/|  |__\______   \___.__."
print	" \_____  \ |  |  \|     ___<   |  |"
print	" /        \|   Y  \    |    \___  |"
print	"/_______  /|___|  /____|    / ____|"
print	"        \/      \/          \/     "
print	""
print	"# search_shodan.py #"
print	"# Search SHODAN and print a list of IPs matching the query #"
print	"# gunma, gunma.rootedker.nl #"
print	""

# Input validation
if len(sys.argv) == 1:
	print 'Usage: %s <search query, eg. "netgear">' % sys.argv[0]
	sys.exit(1)
	

# Wrap the request in a try/ except block to catch errors
try:
        # Search Shodan
        results = api.search(' '.join(sys.argv[1:]))

        # Show the results
        print 'Results found: %s' % results['total']
        for result in results['matches']:
                print 'IP: %s' % result['ip']
                print result['data']
                print ''
except Exception, e:
        print 'Error: %s' % e
