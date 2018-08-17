import urllib2
import selenium
import time
import re
import csv

from bs4 import BeautifulSoup
from selenium import webdriver


neighborhoodListURL = "https://dynamic.stlouis-mo.gov/citydata/newdesign/statsselector.cfm?type=data&geo=neigh"

driver = webdriver.Chrome()
driver.get(neighborhoodListURL)

# Names of all 79 neighborhoods in St. Louis
def get_neighborhoods():

	neighborhoods = []

	content = urllib2.urlopen(neighborhoodListURL).read()
	soup = BeautifulSoup(content, "html.parser")

	select = soup.find("select", {"name": "neighselect"})
	options = select.find_all("option")

	for option in options:
		neighborhoods.append({"name": option.text, "id": option['value']})

	# neighborhoods = [ {"name": option.text, "id": option['value']} for option in options ]

	return neighborhoods


def get_data(soup, nhd_id, nhd_name):

	nhd_data = []

	# Parent element
	table__rows = soup.find_all('tr', attrs={'class':'blue12point'})

	for table__row in table__rows:

		# Children of table__row
		row__cells = table__row.find_all("td")


		# For each page, get the following data:
		row__year = row__cells[0].text
		row__total = row__cells[1].text
		row__residential = row__cells[2].text
		row__commercial = row__cells[3].text

		nhd_data.append( 
			[ nhd_id, nhd_name, row__year, row__total, row__residential, row__commercial ]
		)

	return nhd_data


# Create the spreadsheet
def make_spreadsheet( out_data ):

	with open("vacant.csv", "wb") as f:
		writer = csv.writer(f)
		for row in out_data:
			writer.writerow( row )


def open_pages():

	neighborhoods = get_neighborhoods()

	out_data = [ ['nhd_id','nhd_name','year','total','residential','commercial'] ]

	for neighborhood in neighborhoods:

		time.sleep(2)

		url = 'http://dynamic.stlouis-mo.gov/citydata/newdesign/output.cfm?geo=neigh&subcat=&neighselect=' + neighborhood['id'] + '&reports=f'

		driver.get(url)
		content = driver.page_source

		soup = BeautifulSoup(content, "html.parser")

		data = get_data(soup, neighborhood['id'], neighborhood['name'])

		out_data += data

	print out_data

	make_spreadsheet( out_data )

open_pages()