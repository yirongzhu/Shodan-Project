'''
Created on Feb 22, 2014

@author: Zhu Yirong
'''
from shodan import WebAPI

SHODAN_API_KEY = "CUn5UHoYD784Z3AlfUdvulRjiP2oUBfm"

api= WebAPI(SHODAN_API_KEY)

# This example retrieves detailed information from a list of hosts, and count how many of them are accessible.
count=0
for i in range(41,50):
    try:
        host = api.host('217.140.75.'+str(i))
        print 'accessing host %s' % host['ip']
        print '%s' % host # print the entire jasonobject for the host.
        count+=1

    except Exception, e:
        print 'Error: %s 217.140.75.%s' % (e,i)

print 'total # of available hosts in the range is %s' % count