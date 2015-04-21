# MainModule.py - Driver that executes functions from all other modules. Gets the comments from
#	the latest episode.
# Necessary things:
# 	Firefox Browser, Python, pip, Selenium, Mechanize, other modules

# Import other modules
import Browser
import GetCrunchyComments
import GetCrunchyShows
import MakeCrunchyDirs
import MakeCrunchyCSV
import os
import sys
sys.path.insert(0, '../')
from Classifiers import CrunchyFillerClassifier

#------------------------------------------------------------------------
# getLatestEpisode - Extracts the latest episode for the specified show
#
# input: browser, showURL
# output: Tuple containing an episode link and corresponding title
#
# episodeContainer: div that contains the episode attributes (including the links)
# episodeLinks: html element that contains link to the episode
# episodeLink: Single link to an episode
# episodeNumber: html attribute that contains the episode number
# episodeTitle: html element that contains the title of the episode
#------------------------------------------------------------------------
def getLatestEpisode(browser, showURL):
	browser.get(showURL)

	# look for ul class="portrait-grid" which contains the episode links and titles
	episodeContainer = browser.find_element_by_class_name("portrait-grid")
	episodeLinks = episodeContainer.find_element_by_tag_name('a')

	# compile the list of the episode links, #s, and titles
	episodeLink = episodeLinks.get_attribute('href')
	episodeNumber = episodeLinks.find_element_by_css_selector('span.series-title.block.ellipsis')
	episodeNumber = episodeNumber.text.replace(" ", "-")
	episodeTitle = episodeLinks.find_element_by_class_name('short-desc') #div with episode title
	episodeTitle = episodeTitle.text

	# tuple containing the episode title and corresponding link
	return (episodeLink, episodeTitle)

#------------------------------------------------------------------------
# extractData - Extracts comments from latest episode
#
# input: browser
# output: None
#
# baseURL: the crunchyroll website URL
# listOfShowTitles: list of (cleaned) show titles
# showURL: URL for a show's page on Crunchyroll
# episodeLinkAndTitle: Tuple containing an episode's title and corresponding link
# episodeLink: Episode's link (separated from the episodeLinkAndTitle tuple)
# episodeTitle: An episode's link (separated from the episodeLinkAndTitle tuple)
# showsDirectory: parent directory for all show subdirs
# episodesDir: Directory for individual shows
# listOfComments: List of comments for each episode of each show
#------------------------------------------------------------------------
def extractData(show):
    # Run the module
    browser = Browser.setupBrowser()
    baseURL = 'http://www.crunchyroll.com/'

	# Get the shows whose episode comments we want to extract
    listOfShowTitles = GetCrunchyShows.getShows(show) #returns list of showtitles

    for showTitle in listOfShowTitles:

        showURL = baseURL + showTitle

		# Get the episodes (urls) for the show we specified
        episodeLinkAndTitle = getLatestEpisode(browser, showURL)
		
        episodeLink = episodeLinkAndTitle[0]
        episodeTitle = episodeLinkAndTitle[1]

		# Declare parent directory for all the shows
        showsDirectory = 'Shows/'

		# create sub-directory for the eindividual shows
        episodesDir = MakeCrunchyDirs.makeDirectories(showsDirectory+showTitle)

		# Extract the comments
        listOfComments = GetCrunchyComments.getComments(browser, episodeLink)

		# Write the list of comments and episodes to a csv file
        MakeCrunchyCSV.writeToCSV(episodeTitle, episodesDir, listOfComments)

    #Classify the episode
    episodeClass = CrunchyFillerClassifier.classifyFillerOrCanon(0.25, listOfComments)

    browser.quit()
    print "Done."
