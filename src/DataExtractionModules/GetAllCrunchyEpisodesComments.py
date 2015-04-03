# GetPreviousCrunchyEpisodes.py - Get all episodes to date for the specified show

import Browser
import GetCrunchyComments
import GetCrunchyShows
import MakeCrunchyDirs
import GetCrunchyComments
import MakeCrunchyCSV
import GetAllCrunchyEpisodes

def getAllEpisodes(browser):
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

	# Get the comments for each of the episodes ***NOTE WE ONLY CLASSIFY THE LATEST EPISODE.***
	for episodeLink in listOfEpisodeLinks:

		#make a directory for each episode to store the comments
		episodesDir = MakeCrunchyDirs.makeDirectories(showsDirectory+showTitle)

		#Extract the comments
		listOfComments = GetCrunchyComments.getComments(browser, episodeLink)

		# Write the list of comments and episodes to a csv file
		MakeCrunchyCSV.writeToCSV(listOfEpisodeTitles[index], episodesDir, listOfComments)
		index = index +1

	print "Done getting all episode comments for." + showTitle

browser = Browser.setupBrowser()
getAllEpisodes(browser)