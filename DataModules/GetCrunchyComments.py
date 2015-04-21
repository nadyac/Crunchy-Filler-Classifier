# GetcrunchyComments.py - Extracts user comments using the browser to query server
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getComments(browser, episodeURL):
	episodeCommentsURL = episodeURL + '/comments'
	browser.get(episodeCommentsURL)
	listOfComments = []

	# wait for the comments page to finish loading the comments
	WebDriverWait(browser, 5)

	# Get the DOM element that contains the comments
	elems = browser.find_elements_by_class_name("guestbook-body")
	i = 0
	for n in elems:
		try:
			i = i + 1
			comment = n.text
			print comment
			
		except UnicodeError as e:
			comment = "UNICODE ERROR IN COMMENT"
			print str(i) + "UNICODE ERROR IN COMMENT"
			pass
		listOfComments.append(comment)

	return listOfComments


