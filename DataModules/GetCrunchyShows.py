# GetCrunchyShows - Tells the system which shows to track and get episode comments for
# To get the shows, pass the browser to the function, go to the shows page, and extract them
# Note there are lots of shows, so pick the ones that users wish to track

import ReplaceCharsInString

# Gets a show or list of shows and returns it
def getShows(show):
	"""NOTE: actual show variable will be obtained dynamically from CR or the db
	"""
	#show1 = 'kuroko\'s Basketball' 
	#show2 = 'Blue Exorcist'
	#show3 = 'yona of the dawn'
	#show4 = 'Angel Beats'
	#show5 = 'Naruto Shippuden'
	#show6 = 'Bleach'
	#show7 = 'Another'
	#show8 = 'Attack on Titan'
	#show9 = 'silver spoon'
	#show10 = 'Sword Art Online'

	#random shows
	#show11 = 'Break Ups'
	#show12 = 'Fairy Tail'
	#show13 = 'ixion saga DT'
	#show14 = 'GLasslip'
	#show15 = 'karasuma kyoko no jikenbo manga 25'
	#show16 = 'kokoro connect'
	#show17 = 'magic kaito 1412'
	#show18 = 'oreimo'
	#show19 = 'Durarara'
	#show20 = 'rurouni kenshin'
	
	listOfRawShowTitles = [show]
	listOfCleanShowTitles =[]

	for show in listOfRawShowTitles:
		show = ReplaceCharsInString.cleanString(show)
		listOfCleanShowTitles.append(show)

	#return list of shows without weird chars
	return listOfCleanShowTitles


