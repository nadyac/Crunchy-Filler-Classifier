'''
Browser.py - Browser initiation module
Description:
	This module instantiates a Firefox Browser with basic settings

Inputs: None 
Output: Browser

Necessary things:
	Firefox Browser, Python, pip, Selenium, Mechanize

'''
# Selenium imports
import mechanize
from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from selenium.webdriver.common.keys import Keys
import os
import re

# Set up Selenium and the browser params
# NOTE: this assumes Firefox is installed
def setupBrowser():
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(False)
	br.addheaders = [{'User-agent', 'Firefox'}]

	browser = webdriver.Firefox()
	return browser