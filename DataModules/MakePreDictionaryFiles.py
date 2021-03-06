# MakePreDictionary.py - create file containing all words in comments
#
import os
import sys
import csv
import ReplaceCharsInString

# for each csv file, read the contents and create a file with all the useful words
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

						# Create and open pre-dictionary file for writing
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

								# filter out words that don't add to the meaning of the comment
								if word != 'i' and word != 'this' and word != 'that' and \
								word != 'they' and word != 'we' and word != 'you' and \
								word != 'me' and word != 'he' and word != 'she' and word != 'it' \
								and word != 'them' and word != 'to' and word != 'for' and \
								word != 'with' and word != 'have' and word != 'be' and \
								word != 'been' and word != 'a' and word != 'or' and word != 'if'\
								and word != 'are' and word != 'when' and word != 'the' and \
								word != 'and' and word != 'in' and word != 'my' and word.find('@') == -1\
								and word != 'at' and word != 'on' and word != 'there' and \
								word != 'their' and word != 'theyre' and word != 'how' and word != 'as' \
								and word != 'if' and word != 'was' and word != 'has' and word != 'had' \
								and word != 'is' and word != " " and word.find('=') == -1 and word.find('_') == -1 \
								and word.find('<') == -1 and word.find('>') == -1 and len(word) > 1 \
								and word != 'of' and word != 'from':

									# Unite filler and flashback counts since they tend to be correlated
									if word.find('filler') != -1 or word.find('flashback') != -1 or word.find("recap") != -1:
										fillerCount +=1

										if incrementFlag == False:
											commentsWithFillerWords += 1
											incrementFlag = True # so we won't increment anymore during this comment

									#write word to list
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
