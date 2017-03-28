import csv
import requests
from BeautifulSoup import BeautifulSoup 
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

years = ['2014-2015', '2015-2016']

for year in years:
    print year
    response = requests.get("https://columbian.gwu.edu/" + year)
    html = response.content

    soup = BeautifulSoup(html)
    table = soup.find('table')

    list_of_rows = []
    for row in table.findAll('tr')[1:]:
        list_of_cells = []
        list_of_cells.append(year)
        for cell in row.findAll('td'):
            list_of_cells.append(cell.text.encode('utf-8'))
        list_of_rows.append(list_of_cells)


outfile = open("grants4.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Year","Department", "Faculty", "Sponsor", "Title"])
writer.writerows(list_of_rows)