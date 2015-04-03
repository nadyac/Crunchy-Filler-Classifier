# MakeCrunchyCSV.py - Writes show data to CSV file
# pre-condition: the csv files will be created only if their directory exists
# if their parent directory has not been created, then the module that creates it will be called
import csv
import os
import sys
import MakeCrunchyDirs
from os import chdir

# fileName - Name of csv file. Should be same as episode title,i.e. episodeTitle.csv
# dirPath - directory location where the csv file will be created
#			should be Shows/Show-Title/
# listOfComments - all the comments that will go into each corresponding csv file
#				i.e. episode1 comments will go into episode1.csv

def writeToCSV(csvFileName, dirPath, listOfComments):

	# clear any unusual characters in the episode title before using it as the csv file name
	csvFileName = csvFileName.replace(" ", "-") # replace whitespace in the title with '-'
	csvFileName = csvFileName.replace("'", "")
	csvFileName = csvFileName.replace(".", "")
	csvFileName = csvFileName.replace(":", "")
	csvFileName = csvFileName.replace("?", "")
	csvFileName = csvFileName.replace("!", "")
	csvFileName = csvFileName.replace(",", "")
	csvFileName = csvFileName.replace("(", "")
	csvFileName = csvFileName.replace(")", "")

	csvFileName = csvFileName + '.csv'
	print "created " + csvFileName

	# if the directory for the csv file doesn't exist, create it, then write to it
	if os.path.exists(dirPath):
		with open(os.path.join(dirPath, csvFileName), 'w') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=",")

			for comment in listOfComments:
				try:
					line = comment + "\n"
					#csvfile.write(line.encode('utf-8')) #ex: filler <comment> this works but takes a long time
					csvfile.write(line)
				except UnicodeError as err:
					pass
	else:
		print "in else statement."
		MakeCrunchyDirs.makeDirectories(dirPath)
		writeToCSV(csvFileName, dirPath, listOfComments)

# for testing
#commentsList = ['how cool', 'that episode was nice']
#writeToCSV('episode title', 'Shows/Angel-Beats/',commentsList)