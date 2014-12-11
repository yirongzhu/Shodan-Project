'''
Created on Feb 24, 2014

@author: Zhu Yirong
'''
import xlsxwriter
from shodan import WebAPI

SHODAN_API_KEY = "CUn5UHoYD784Z3AlfUdvulRjiP2oUBfm"

api = WebAPI(SHODAN_API_KEY)

workbook = xlsxwriter.Workbook('VulnerableLocation.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

worksheet.write('A1','IP',bold)            
worksheet.write('B1','Latitude',bold)
worksheet.write('C1','Longitude',bold)
worksheet.write('D1','Country',bold)
worksheet.write('E1','Port',bold)


row = 1

try:
        # Search Shodan
        results = api.search('port:32764')

        # Show the results
        print results
        
        for result in results['matches']:   
            ipaddress = result['ip']
            latitude = result['latitude']
            longitude = str(result['longitude'])
            country = result['country_name']
            port = result['port']
            worksheet.write(row, 0, ipaddress)
            worksheet.write(row, 1, latitude)
            worksheet.write(row, 2, longitude)
            worksheet.write(row, 3, country)
            worksheet.write(row, 4, port)
            row = row + 1
            
except Exception, e:
    print 'Error: %s' % e
# Write some numbers, with row/column notation.
#worksheet.write(2, 0, 123)
#worksheet.write(3, 0, 123.456)
# Insert an image.
#worksheet.insert_image('B5', 'logo.png')
workbook.close()
print "Done"