# LatestEpisodeGetter.py - Get the latest episode on Crunchyroll for the given show

def getLatestEpisodes(browser, showURL):
	browser.get(showURL)

	# look for ul class="portrait-grid" which contains the episode links and titles
	episodeContainer = browser.find_element_by_class_name("portrait-grid")
	episodeLinks = episodeContainer.find_elements_by_tag_name('a')

	# compile the list of the episode links, #s, and titles
	episodeLink = n.get_attribute('href')
	episodeNumber = n.find_element_by_css_selector('span.series-title.block.ellipsis')
	episodeNumber = episodeNumber.text.replace(" ", "-")
	episodeTitle = n.find_element_by_class_name('short-desc') #div with episode title
	episodeTitle = episodeTitle.text

	return (episodeLink, episodeTitle)
