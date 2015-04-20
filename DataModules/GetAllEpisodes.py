# GetPreviousCrunchyEpisodes.py - Main module for getting all episodes for the specified show

import Browser
import GetCrunchyComments
import GetCrunchyShows
import MakeCrunchyDirs
import MakeCrunchyCSV

'''------------------------------------------------------------------------
getLatestEpisode - Extracts the latest episode for the specified show

input: browser, showURL
output: Tuple containing an episode link and corresponding title

episodeContainer: div that contains the episode attributes (including the links)
episodeLinks: html element that contains link to the episode
episodeLink: Single link to an episode
episodeNumber: html attribute that contains the episode number
episodeTitle: html element that contains the title of the episode
------------------------------------------------------------------------
'''
def getEpisodes(browser, showURL):
	browser.get(showURL)

	# look for ul class="portrait-grid" which contains the episode links and titles
	episodeContainer = browser.find_element_by_class_name("portrait-grid")
	episodeLinks = episodeContainer.find_elements_by_tag_name('a')
	#episodeNumber = n.find_element_by_class_name('series-title block ellipsis') #div with the episode #
	listOfEpisodeLinks = []
	listOfEpisodeTitles = []

	# compile the list of the episode links, #s, and titles
	for n in episodeLinks:
		episode = n.get_attribute('href')
		episodeNumber = n.find_element_by_css_selector('span.series-title.block.ellipsis')
		episodeNumber = episodeNumber.text.replace(" ", "-")
		episodeTitle = n.find_element_by_class_name('short-desc') #div with episode title
		episodeTitle = episodeTitle.text

		listOfEpisodeTitles.append(episodeNumber + "-" + episodeTitle)
		listOfEpisodeLinks.append(episode)

	return (listOfEpisodeLinks, listOfEpisodeTitles)

'''
------------------------------------------------------------------------
getAllEpisodes - Extracts comments from latest episode

input: browser
output: None

baseURL: the crunchyroll website URL
listOfShowTitles: list of (cleaned) show titles
showURL: URL for a show's page on Crunchyroll
episodeLinkAndTitle: Tuple containing an episode's title and corresponding link
episodeLink: Episode's link (separated from the episodeLinkAndTitle tuple)
episodeTitle: An episode's link (separated from the episodeLinkAndTitle tuple)
showsDirectory: parent directory for all show subdirs
episodesDir: Directory for individual shows
listOfComments: List of comments for each episode of each show
------------------------------------------------------------------------
'''
def getAllEpisodes(browser):
	baseURL = 'http://www.crunchyroll.com/'

	# Get the shows whose episode comments we want to extract
	listOfShowTitles = GetCrunchyShows.getShows()

	# run through the list of show titles, get their complete episode list and comments
	# for each episode
	for show in listOfShowTitles:
		showTitle = show

		showURL = baseURL + showTitle

		# Get the episodes (urls) for the show we specified
		episodeLinksAndTitles = getEpisodes(browser, showURL)

		listOfEpisodeLinks = episodeLinksAndTitles[0]
		listOfEpisodeTitles = episodeLinksAndTitles[1]

		# Declare parent dir for all the shows
		showsDirectory = 'Shows/'
		index = 0;

		# Get the comments for each of the episodes
		for episodeLink in listOfEpisodeLinks:

			#make a directory for each episode to store the comments
			episodesDir = MakeCrunchyDirs.makeDirectories(showsDirectory+showTitle)

			#Extract the comments
			listOfComments = GetCrunchyComments.getComments(browser, episodeLink)

			# Write the list of comments and episodes to a csv file
			MakeCrunchyCSV.writeToCSV(listOfEpisodeTitles[index], episodesDir, listOfComments)
			index += 1

		print "Done getting all episode comments for " + showTitle
	browser.quit()
	print "Done getting all the shows."

browser = Browser.setupBrowser()
getAllEpisodes(browser)