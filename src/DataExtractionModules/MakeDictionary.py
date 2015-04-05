# MakeDictionery.py - create dictionary of all words in comments
import os
import sys
import csv

# for each csv file, read the contents and create a dict file
def makeDict(csvFileName, dirPath):

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

						with open(os.path.join(subdir, 'dict'+ file), 'w') as dictfile:
							writer = csv.writer(dictfile, delimiter=' ')

							# create dictionary to store word and value pairs
							counts = {}

							# read from CSVfile and write to dictfile
							csvreader = csv.reader(csvfile, delimiter= ' ')
							# read all the comments in each csv file
							commentsCount = 0;
							fillerCount = 0;

							for comments in csvreader:

								commentsCount += 1

								for words in comments:

									# clean the words in the csvfile to remove unncessary words and
									# characters/punctuations
									word = words.lower()

									word = word.replace(":", "")
									word = word.replace("]", "")
									word = word.replace("^", "")
									word = word.replace("'", "")
									word = word.replace(",", "")
									word = word.replace("!", "")
									word = word.replace(".", "")
									word = word.replace ("?", "")

									if word != 'i' and word != 'this' and word != 'that' and \
									word != 'they' and word != 'we' and word != 'you' and \
									word != 'me' and word != 'he' and word != 'she' and word != 'it' \
									and word != 'them' and word != 'to' and word != 'for' and \
									word != 'with' and word != 'have' and word != 'be' and \
									word != 'been' and word != 'a' and word != 'or' and word != 'if'\
									and word != 'are' and word != 'when' and word != 'the' and \
									word != 'and' and word != 'in' and word != 'my':

										#write to dict
										counts[word] = counts.get(word, 0) + 1

										if word.find('filler') != -1:
											fillerCount +=1
							try:
								print "total comments: " + str(commentsCount) + " comments that mention the word filler: " +  str(fillerCount) + "\n"
								writer.writerow("total comments: " + str(commentsCount) + " comments that mention the word filler: " +  str(fillerCount))
								writer.writerow("\n")
								writer.writerow(counts.items())
							except KeyError as err:
								print "KeyError occurred with key."
								pass

					csvfile.close()
					dictfile.close()
	else:
		print "directory Shows\ does NOT exist."
	print "Done creating dictionary files."

csvFileName ="hehe"
dirPath = 'Shows\\'
makeDict(csvFileName, dirPath)
