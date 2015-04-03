# MainModule.py - Driver that executes functions from all other modules
# Necessary things:
# 	Firefox Browser, Python, pip, Selenium, Mechanize,  requests lib, other modules

# Import other modules
import Browser
import GetCrunchyComments
import GetCrunchyShows
import GetAllCrunchyEpisodes
import LatestEpisodeGetter
import MakeCrunchyDirs
import MakeCrunchyCSV
import GetAllCrunchyEpisodes
import LatestEpisodeGetter

# Gets comments from latest episode
def extractData(browser):
	baseURL = 'http://www.crunchyroll.com/'

	# Get the shows whose episode comments we want to extract
	listOfShowTitles = GetCrunchyShows.getShows()
	showTitle = listOfShowTitles[0] # loop through these later?*******************

	showURL = baseURL + showTitle

	# Get the episodes (urls) for the show we specified
	#episodeLinksAndTitles = GetCrunchyEpisodes.getEpisodes(browser, showURL)
	episodeLinkAndTitle = LatestEpisodeGetter.getLatestEpisode(browser, showURL)
	
	episodeLink = episodeLinkAndTitle[0]
	episodeTitle = episodeLinkAndTitle[1]

	# Create directories for each show and subdirs for each episode on the list
	showsDirectory = 'Shows/'
	index = 0

	# Get the latest episode and place it in a directory
	# make a directory for the episode to store the comments
	episodesDir = MakeCrunchyDirs.makeDirectories(showsDirectory+showTitle)

	#Extract the comments
	listOfComments = GetCrunchyComments.getComments(browser, episodeLink)

	# Write the list of comments and episodes to a csv file
	MakeCrunchyCSV.writeToCSV(episodeTitle, episodesDir, listOfComments)

	print "Done."

browser = Browser.setupBrowser()
extractData(browser)