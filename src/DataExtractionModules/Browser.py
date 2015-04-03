# Browser.py - Browser initiation module
# Necessary things:
# 	Firefox Browser, Python, pip, Selenium, Mechanize,  requests lib, other modules

# Import other modules
import GetCrunchyComments
import GetCrunchyShows
import GetCrunchyEpisodes
import LatestEpisodeGetter
import MakeCrunchyDirs
import MakeCrunchyCSV

# Selenium imports
import mechanize
import requests
import time
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