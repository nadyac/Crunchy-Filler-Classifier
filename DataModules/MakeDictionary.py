# MakeDictionary.py - create dictionary of all words in comments
import os
import sys
import csv
import ReplaceCharsInString

# for each csv file, read the contents and create a dict file
def makeDict(dirPath):

	# check that path exists, if so, continue, else stop
	if os.path.exists(dirPath):

		#walk through the directory into the subdirs to find files
		for subdir, dirs, files in os.walk(dirPath):
			for file in files:

				if file.find('dict') == -1:
					print "***********" + file + "************"

				# Check if the dictionary file already exists (overwrites it if it does)
				if os.path.exists(os.path.join(subdir, file)) and file.find('dict') is -1:

					# Open each CSV file and read its contents
					with open(os.path.join(subdir, file), 'r') as csvfile:

						# Create and open dictionary file for writing
						dictfile = open(os.path.join(subdir, 'dict'+ file), 'w')

						wordList =[]

						# read from CSVfile and write to dictfile
						csvreader = csv.reader(csvfile, delimiter= ' ')
						# read all the comments in each csv file
						commentsCount = 0;
						fillerCount = 0;
						wordCount = 0;
						commentsWithFillerWords = 0 #this is also a feature

						for comments in csvreader:

							commentsCount += 1
							incrementFlag = False # prevents commentsWithFillerWords from being incremented more than once per comment

							for words in comments:

								# clean the words in the csvfile to remove unncessary words and
								# characters/punctuations
								word = words.lower()
								word = ReplaceCharsInString.cleanString(word)
								word = word.replace ("-", "")

								# Unite filler and flashback counts since they tend to be correlated
								if word.find('filler') != -1 or word.find('flashback') != -1 or word.find("recap") != -1:
									fillerCount +=1

									if incrementFlag == False:
										commentsWithFillerWords += 1
										incrementFlag = True # so we won't increment anymore during this comment

								#write key word to dictionary along with its key value
								wordList.append(word)
								# increment word count so we know how many words are in all the comments for the episode
								wordCount += 1
						try:
							print "total comments: " + str(commentsCount) + " times the word filler or flashback mentioned: " + \
							str(fillerCount) + " comments with filler words: " + str(commentsWithFillerWords) + "\n"
							dictfile.write("total comments:" + "\n")
							dictfile.write(str(commentsCount))
							dictfile.write("\n")
							dictfile.write("comments with filler words:" + "\n")
							dictfile.write(str(commentsWithFillerWords) + "\n")
							dictfile.write("total mentions of filler or flashback:" + "\n")
							dictfile.write(str(fillerCount))
							dictfile.write("\n")
							dictfile.write("total words:" + "\n")
							dictfile.write(str(wordCount))
							dictfile.write("\n")
							dictfile.write("\n")
							dictfile.write(str(wordList).translate(None, '[]()\','))

						except KeyError as err:
							print "KeyError occurred with key."
							pass

					csvfile.close()
					dictfile.close()
	else:
		print "directory Shows\ does NOT exist."
	print "Done creating dictionary files."

dirPath = 'Shows\\'
makeDict(dirPath)
