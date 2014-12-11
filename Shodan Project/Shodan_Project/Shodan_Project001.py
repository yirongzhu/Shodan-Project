'''
Created on Feb 22, 2014

@author: Zhu Yirong
'''

from shodan import WebAPI
SHODAN_API_KEY = "CUn5UHoYD784Z3AlfUdvulRjiP2oUBfm"
api= WebAPI(SHODAN_API_KEY)
# Wrap the request in a try/ except block to catch errors
try:
    # Search Shodan
    results = api.search('apache')
    print results
    # Show the results
    for result in results['matches']:
        if '200 OK' in result['data']:
            print 'IP: %s' % result['ip']

except Exception, e:
    print 'Error: %s' % e
