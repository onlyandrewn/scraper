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


url = "https://dynamic.stlouis-mo.gov/citydata/newdesign/statsselector.cfm?type=data&geo=neigh"

driver = webdriver.Firefox()
driver.get(url)

# time.sleep(5)

# Empty arrays where the data will be stored

# years = []

# vacant_total = []
# vacant_residential = []
# vacant_commercial = []

# This is a script from the St. Louis Post-Dispatch
# SELECT OPTIONS



# def get_neighborhoods():
# 	# Names of all 79 neighborhoods in St. Louis
# 	neighborhoods = []

# 	content = urllib2.urlopen(url).read()
# 	soup = BeautifulSoup(content, "html.parser")

# 	neighborhoods.append(soup.find("select", {"name": "neighselect"}).getText())

# 	for neighbourhood in neighborhoods:
# 		print neighbourhood

# get_neighborhoods()


def make_selection():
	# Open new window

	# for n in neighborhoods:
	# 	# Values

	# Select a neighborhood
	neighborhood_name = driver.find_element_by_xpath("//option[@value='51']")
	neighborhood_name.click()
	time.sleep(5)

	# Select vacant buildings
	vacant = driver.find_element_by_xpath("//option[@value='f']")
	vacant.click()
	time.sleep(5)

	# Hit the submit button
	submit = driver.find_element_by_xpath("//input[@type='submit']")
	submit.click()
	time.sleep(5)

make_selection()



def get_data():

	html = driver.page_source
	soup = BeautifulSoup(html, "html.parser")

	# neighbourhood_value = []
	# # neighborhoods = soup.find("select", {"name": "neighselect"}).getText()

	# table__headers = soup.find_all('tr', attrs={'class':'style1'})
	# # print table__headers

	# Parent element
	table__row = soup.find_all('tr', attrs={'class':'blue12point'})
	print table__row

	# # Children of table__row
	# table__year = table__row.find_all("td")
	# table__total = table__row.find_all("td")
	# table__residential = table__row.find_all("td")
	# table__commercial = table__row.find_all("td")

	# print table__year
	# print table__total
	# print table__residential
	# print table__commercial

get_data()




# AFTER OPTIONS SELECTED (ON AN INDIVIDUAL NEIGHBORHOOD PAGE)
# FOR EACH NEIGHBOUR LOOP OVER THE FOLLOWING DATA

# This should give you Year, Total, Residential, Commercial
# table__headers = soup.find("tr", {"class", "style1"}).find_all("td", recursive = False).getText()
# table__headers = soup.find_all("tr")

# table = soup.findAll('table', 'class': '')






# CREATE THE SPREADSHEET

# def make_spreadsheet():

# 	# .append(neighborhoods)
# 	# .append(years)

# 	# .append(vacant_total)
# 	# .append(vacant_residential)
# 	# .append(vacant_commercial)

# 	with open("vacant.csv", "w") as f:
# 		writer = csv.writer()
# 		writer.writerow()

# make_spreadsheet()