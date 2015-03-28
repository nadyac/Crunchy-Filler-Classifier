# MakeCrunchyDirectories.py - Create the necessary directories to store show data
import os
import sys

def makeDirectories(dirPath):
	# check if Shows directory exists, if not make it and the show subdir
	if not os.path.exists(dirPath):
		os.makedirs(dirPath, 0666);
		print "directory " + dirPath + " has been created."
	return dirPath
