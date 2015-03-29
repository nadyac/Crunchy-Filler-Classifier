# GetCrunchyShows - Tells the system which shows to track and get episode comments for
# To get the shows, pass the browser to the function, go to the shows page, and extract them
# Note there are lots of shows, so pick the ones that users wish to track

def getShows():
	#show = 'kuroko\'s Basketball' 
	#show = 'yona of the dawn'
	#show = 'Angel Beats'
	show = 'Naruto Shippuden'
	#show = 'silver spoon'
	"""NOTE: actual show variable will be obtained dynamically from CR
	actual show variable needs to be scanned for illegal characters (apostrophes)
	"""
	show = show.replace(" ", "-") # replace whitespace in the title with -
	show = show.replace("'", "")
	show = show.replace("/", "")
	show = show.replace("!", "")
	show = show.replace(",", "")
	show = show.replace(".", "")

	listOfShows = []
	listOfShows.append(show) #eventually will loop through shows 
	return listOfShows