'''
Created on Feb 23, 2014

@author: Zhu Yirong
'''
import xlsxwriter
from shodan import WebAPI

SHODAN_API_KEY = "CUn5UHoYD784Z3AlfUdvulRjiP2oUBfm"
api= WebAPI(SHODAN_API_KEY)
# Wrap the request in a try/ except block to catch errors
try:
    # Search in Shodan that the vulnerable port: 32764
    results = api.search('port:32764')
    # Show the results of details of these vulnerable_ip
    vulnerable_Ip = []
    vul_Country = []
    vul_Latitude = []
    vul_Longitude = []
    for result in results['matches']:
        vulnerable_Ip.append(result['ip']) 
        vul_Country.append(result['country_name'])
        vul_Latitude.append(result['latitude'])
        vul_Longitude.append(result['longitude'])
    print 'The vulnerable ip addresses are %s' % vulnerable_Ip
    print 'The number of vulnerable ip addresses are %s' % len(vulnerable_Ip)
    
    # Count the number of vulnerable port:32764 in each country
    country_details = {}
    for vul in vul_Country:
        if vul not in country_details:
            country_details[vul] = 1
        else:
            country_details[vul] += 1
    print 'The distribution of vulnerable addresses: %s' % country_details
    
    # Get the ip addresses and the number of devices that could be intruded into right now.
    ipbreak = set()
    ipbreaklocation = set()
    for ip in vulnerable_Ip:
        host = api.host(ip)
        for port in host['data']:
            if port['port'] == 80:
                ipbreak.add(host['ip'])
                if host['latitude'] != None and host['longitude'] != None:
                    ipbreaklocation.add((host['latitude'],host['longitude']))
                    
    print 'The ip addresses of devices that could be intruded are in this %s' % ipbreak
    print 'The number of devices that could be intruded are %s out of 100' % len(ipbreak)
    print 'The locations of devices that could be identified are in this %s' % ipbreaklocation
    print 'The number of locations of devices that could be identified are %s' % len(ipbreaklocation)

except Exception, e:
    print 'Error: %s' % e


workbook = xlsxwriter.Workbook('Vulnerable32764.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

worksheet.write('A1','Vulnerable_IP',bold)            
worksheet.write('B1','Vulnerable_Latitude',bold)
worksheet.write('C1','Vulnerable_Longitude',bold)
worksheet.write('D1','Target_IP',bold)
worksheet.write('E1','Target_Latitude',bold)
worksheet.write('F1','Target_Longitude',bold)
worksheet.write('G1','Country',bold)
worksheet.write('H1','NumInCountry',bold)


row = 1

try:
    for vul_ip in vulnerable_Ip:
        worksheet.write(row, 0, vul_ip)
        row += 1
        
    row = 1
    
    for vul_lati in vul_Latitude:
        worksheet.write(row, 1, vul_lati)
        row += 1
    
    row = 1
    
    for vul_longi in vul_Longitude:
        worksheet.write(row, 2, vul_longi)
        row += 1
    
    row = 1
    
    for target_ip in ipbreak:
        worksheet.write(row, 3, target_ip)
        row += 1
    
    row = 1
    
    for target_location in ipbreaklocation:
        worksheet.write(row, 4, target_location[0])
        row += 1
    
    row = 1
        
    for target_location in ipbreaklocation:
        worksheet.write(row, 5, target_location[1])
        row += 1
    
    row = 1
    
    for vul_country in country_details:
        worksheet.write(row, 6, vul_country)
        worksheet.write(row, 7, country_details[vul_country])
        row += 1
    
    row = 1
    

except Exception, e:
    print 'Error: %s' % e

workbook.close()
print "Data Inserted"
