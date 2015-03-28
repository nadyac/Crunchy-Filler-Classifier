# MainModule.py - Driver that executes functions from all other modules
# Necessary things:
# 	Firefox Browser, Python, pip, Selenium, Mechanize,  requests lib, other modules

# Import other modules
import GetCrunchyComments
import GetCrunchyShows
import GetCrunchyEpisodes
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
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders = [{'User-agent', 'Firefox'}]

browser = webdriver.Firefox()
baseURL = 'http://www.crunchyroll.com/'

# Get the shows whose episode comments we want to extract
listOfShowTitles = GetCrunchyShows.getShows()
showTitle = listOfShowTitles[0] # loop through these later?*******************

showURL = baseURL + showTitle

# Get the episodes (urls) for the show we specified
episodeLinksAndTitles = GetCrunchyEpisodes.getEpisodes(browser, showURL)

listOfEpisodeLinks = episodeLinksAndTitles[0]
listOfEpisodeTitles = episodeLinksAndTitles[1]

# Create directories for each show and subdirs for each episode on the list
showsDirectory = 'Shows/'
index = 0

# Get the comments for each of the episodes
for episodeLink in listOfEpisodeLinks:

	#make a directory for each episode to store the comments
	episodesDir = MakeCrunchyDirs.makeDirectories(showsDirectory+showTitle)

	#Extract the comments
	listOfComments = GetCrunchyComments.getComments(browser, episodeLink)

	# Write the list of comments and episodes to a csv file
	MakeCrunchyCSV.writeToCSV(listOfEpisodeTitles[index], episodesDir, listOfComments)
	index = index +1

print "Done."