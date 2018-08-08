# Go to http://dynamic.stlouis-mo.gov/citydata/newdesign/statsselector.cfm?type=data&geo=neigh
# Select a neighbourhood
# Select vacant buildings
# Hit submit
# Put the data into a spreadsheet each with its own individual tab
# Year Total Residential Commercial are the headers
# The years range from 1990 - 2018

import selenium
import time
import re

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://dynamic.stlouis-mo.gov/citydata/newdesign/statsselector.cfm?type=data&geo=neigh')


years = []

neighborhoods = []

vacant_total = []
vacant_residential = []
vacant_commercial = []




# Click on the option for neighbourhood
# Click on the option for vacant buildings


# Click on the submit button
# driver.click()
# Input type = submit


# Make a new tab in a spreadsheet
# There should be three csvs total. One that is total, one that is residential and the other that is commercial


# In the spreadsheet, make the headers ... ??? (What is the best way to set up the spreadsheet)

