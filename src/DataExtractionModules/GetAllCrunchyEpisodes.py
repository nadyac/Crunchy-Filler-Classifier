# GetCrunchyEpisodes.py
# For a given show, grab all the latest episodes
# returns a tuple containing two lists, a list of episode links and a list of episode # + titles

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