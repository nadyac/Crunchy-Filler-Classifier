# ReplaceCharsInString.py - Takes a string and removes certain characters from it

# Clean title of any unwanted characters
def cleanString(theString):
	string = theString
	string = string.replace(" ", "-") # replace whitespace in the title with -
	string = string.replace("'", "")
	string = string.replace("/", "")
	string = string.replace("!", "")
	string = string.replace(",", "")
	string = string.replace(".", "")
	string = string.replace("(", "")
	string = string.replace(")", "")
	string = string.replace(":", "")
	string = string.replace("]", "")
	string = string.replace("^", "")
	string = string.replace("?", "")
	string = string.replace("*", "")
	string = string.replace("+", "")
	string = string.replace("%", "")
	string = string.replace("$", "")
	string = string.replace("#", "")
	string = string.replace("@", "")
	string = string.replace("\\", "")
	string = string.replace(">", "")
	string = string.replace("<", "")

	return string