'''
MakeBagOfFillerWords.py - loop through a bunch of pre-dictionary files and extract the words and their counts.
	the point of this is to get the probability of a word showing up in a filler doc
	all the words in this bag come from a sample of known filler episodes.
'''
import os
import sys
import csv
sys.path.insert(0, '../')
from DataModules import ReplaceCharsInString

'''
-------------------------------------------------------------------------------------
makeBagOfFillerWords - reads csv files containing comments and creates a dictionary 
	(key value pairs) that use each word as a key and the frequency as the value

input: dirPath
output: None.

- dirPath: the directory location of the csvfiles we wish to read from 
- counts: Dictionary data structure
- commentsCount: int, stores a running total of comments used for the bag of words
- fillerCount: int, stores the running total of words containing 'filler' or 'flashback'
- wordCount: int, running total of words processed
- commentsWithFillerWords: int, running total of comments with filler words
- dictFile: file, dictionary file conatining key-value pairs
- incrementFlag: int, prevents the commentsWithFillerWords from being incremented more than
	once when a comment contains multiple filler words (so that comment will count as one)
- csvreader: python object that reads csv files (in this case the comments csv files)
- comments: string, a line of comment in the csv files
- word: string, a word in a comment line
------------------------------------------------------------------------------------------
'''
# for each csv file, read the contents and create a dict file
def makeBagOfFillerWords(dirPath):

	# check that path exists, if so, continue, else stop
	if os.path.exists(dirPath):

		# create dictionary to store word and value pairs
		counts = {}
		commentsCount = 0;
		fillerCount = 0;
		wordCount = 0;
		commentsWithFillerWords = 0 #this is also a feature

		#walk through the directory into the subdirs to find files
		for subdir, dirs, files in os.walk(dirPath):
			for file in files:

				# Check if the dictionary file already exists (overwrites it if it does)
				if os.path.exists(os.path.join(subdir, file)) and file.find('dict') is -1:

					# Open each CSV file and read its contents
					with open(os.path.join(subdir, file), 'r') as csvfile:

						# Create and open a file for writing the dictionary
						dictfile = open('BagOfFillerWords.txt', 'w')

						# read from CSVfile and write to dictfile
						csvreader = csv.reader(csvfile, delimiter= ' ')

						# read all the comments in each csv file
						for comments in csvreader:

							# if this episode contains comments with filler words, it could be 
							# a filler, so add increment the comment count
							if commentsWithFillerWords >= 6:
								commentsCount += 1

							incrementFlag = False # prevents commentsWithFillerWords from being incremented more than once per comment

							for words in comments:

								# clean the words in the csvfile to remove unncessary words and
								# characters/punctuations
								word = words.lower()
								word = ReplaceCharsInString.cleanString(word)
								word = word.replace("-", "")

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
								and word.find('<') == -1 and word.find('>') == -1:

									# Unite filler and flashback counts since they tend to be correlated
									if word.find('filler') != -1 or word.find('flashback') != -1 or word.find("recap") != -1:
										fillerCount +=1

										if incrementFlag == False:
											commentsWithFillerWords += 1
											incrementFlag = True # so we won't increment anymore during this comment

									#write key word to dictionary along with its key value
									if fillerCount >= 3: #hand-adjusted
										counts[word] = counts.get(word, 0) + 1

										# increment word count so we know how many words are in all the comments for the episode
										wordCount += 1

		#print counts.items()
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
			dictfile.write(str(counts.items()).translate(None, '()\','))

		except KeyError as err:
			print "KeyError occurred with key."
			pass
		csvfile.close()
		dictfile.close()
	else:
		print "directory " + dirPath + " does NOT exist."
	print "Done creating Bag of filler words txt file."

dirPath = '..\DataModules\Shows\\'
makeBagOfFillerWords(dirPath)
