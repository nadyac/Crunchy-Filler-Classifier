# GetcrunchyComments.py - Extracts user comments using the browser to query server

def getComments(browser, episodeURL):
	episodeCommentsURL = episodeURL + '/comments'
	browser.get(episodeCommentsURL)
	listOfComments = []

	# Get the DOM element that contains the comments
	elems = browser.find_elements_by_class_name("guestbook-body")
	i = 0
	for n in elems:
		try:
			i = i + 1
			comment = n.text
			#print str(i) + " " + comment
		except UnicodeError as e:
			comment = "UNICODE ERROR IN COMMENT"
			print str(i) + "UNICODE ERROR IN COMMENT"
			pass
		listOfComments.append(comment)

	return listOfComments


