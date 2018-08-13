# Go to http://dynamic.stlouis-mo.gov/citydata/newdesign/statsselector.cfm?type=data&geo=neigh
# Select a neighbourhood
# Select vacant buildings
# Hit submit
# Put the data into a spreadsheet each with its own individual tab
# Year Total Residential Commercial are the headers
# The years range from 1990 - 2018

import urllib2 # For opening and reading URLs
import selenium
import time
import re

from bs4 import BeautifulSoup
from selenium import webdriver


neighborhoodListURL = "https://dynamic.stlouis-mo.gov/citydata/newdesign/statsselector.cfm?type=data&geo=neigh"

driver = webdriver.Firefox()
driver.get(neighborhoodListURL)

# Empty arrays where the data will be stored

# data = []
# column_headers = []
# years = []
# vacant_total = []
# vacant_residential = []
# vacant_commercial = []

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

def open_pages():

	# neighborhoods = get_neighborhoods()
	neighborhoods = [{'id': '1'}, {'id': '2'}, {'id': '3'}]

	for neighborhood in neighborhoods[0:1]:

		time.sleep(2)

		url = 'http://dynamic.stlouis-mo.gov/citydata/newdesign/output.cfm?geo=neigh&subcat=&neighselect=' + neighborhood['id'] + '&reports=f'
		print url

		# content = urllib2.urlopen(url).read()
		content = driver.get(url)
		soup = BeautifulSoup(content, "html.parser")

		data = get_data(soup)


		# constructURL()
		# Open web page
		# get_data()


open_pages()

# TO BE REMOVED
# def make_selection():

# 	# Select a neighborhood
# 	neighborhood_name = driver.find_element_by_xpath("//option[@value='51']")
# 	neighborhood_name.click()
# 	time.sleep(5)

# 	# Select vacant buildings
# 	vacant = driver.find_element_by_xpath("//option[@value='f']")
# 	vacant.click()
# 	time.sleep(5)

# 	# Hit the submit button
# 	submit = driver.find_element_by_xpath("//input[@type='submit']")
# 	submit.click()
# 	time.sleep(5)

# make_selection()



# For each page, get the following data:
# The headers (Year, Total, Residential, Commerical)
# The years (1990-2018)
# Number of vacant total buildings
# Number of vacant residential buildings
# Number of vacant commercial buildings

def get_data(soup):

	# html = driver.page_source
	# soup = BeautifulSoup(html, "html.parser")

	# Includes the year, total, residential and commercial
	table__headers = soup.find('tr', attrs={'class':'style1'}).getText()
	print table__headers

	# Parent element
	table__row = soup.find_all('tr', attrs={'class':'blue12point'})
	# print table__row

	# # Children of table__row
	table__year = table__row.find("td")
	# table__total = table__row.find_all("td")
	# table__residential = table__row.find_all("td")
	# table__commercial = table__row.find_all("td")

	print table__year
	# print table__total
	# print table__residential
	# print table__commercial

get_data()


# Create the spreadsheet
# def make_spreadsheet():
	# Column headers should be neighborhood, with the years from 1990-2018
	# There should be three spreadsheets (?): one for total, residential and commercial

	# data.append(neighborhoods)
	# data.append(years)
	# data.append(vacant_total)
	# data.append(vacant_residential)
	# data.append(vacant_commercial)

	# 	with open("vacant.csv", "w") as f:
	# 		writer = csv.writer()
	# 		writer.writerow()

# make_spreadsheet()