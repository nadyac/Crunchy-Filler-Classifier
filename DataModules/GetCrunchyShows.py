# GetCrunchyShows - Tells the system which shows to track and get episode comments for
# To get the shows, pass the browser to the function, go to the shows page, and extract them
# Note there are lots of shows, so pick the ones that users wish to track

import ReplaceCharsInString

# Gets a show or list of shows and returns it
def getShows(show):
	"""NOTE: actual show variable will be obtained dynamically from CR or the db
	"""
	listOfRawShowTitles = [show]
	listOfCleanShowTitles =[]

	for show in listOfRawShowTitles:
		show = ReplaceCharsInString.cleanString(show)
		listOfCleanShowTitles.append(show)

	#return list of shows without weird chars
	return listOfCleanShowTitles


