# FillerClassifier - takes in class priors (P(filler)) and the document (comments)
#	and gives a classification based on the word frequency probabilities in the Bag of Words
#	Current assumes that P(filler) = 0.25 based on limited filler episode data (mostly Naruto episodes)
#	Feature1= ratio of filler comments to non-filler comments, Feature2 = ratio of filler words to non-filler words
#	Document = comments for the unclassified episode
from __future__ import division
import os
import sys
sys.path.insert(0, '../')
from DataModules import ReplaceCharsInString

def classifyFillerOrCanon(ProbabilityOfFiller, document):

	class1 = 'Filler'
	class2 = 'Not Filler'
	RatioOfFillerToCanonComments = 0
	RatioOfFillerToCanonWords = 0

	# create dictionary to store word and value pairs
	counts = {}
	commentsCount = 0;
	fillerCount = 0;
	wordCount = 0;
	commentsWithFillerWords = 0 #this is also a feature

	# read all the comments in each document
	for words in document:

		# if this episode contains comments with filler words, it could be 
		# a filler, so add increment the comment count
		if commentsWithFillerWords >= 1:
			commentsCount += 1

		incrementFlag = False # prevents commentsWithFillerWords from being incremented more than once per comment

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

			# increment word count so we know how many words are in all the comments for the episode
			wordCount += 1

	print " word count: " + str(wordCount)
	print " filler words count " + str(fillerCount)

	print "commentsCount: " + str(commentsCount)
	print "commentsWithFillerWords " + str(commentsWithFillerWords)

	try:
		RatioOfFillerToCanonComments = (commentsWithFillerWords)/(commentsCount)
		RatioOfFillerToCanonWords = (fillerCount)/(wordCount)
		print "Ratio of filler to canon comments: " + str(RatioOfFillerToCanonComments)
		print "Ratio of filler to canon words: " + str(RatioOfFillerToCanonWords)
	except ZeroDivisionError as e:
		print "A wild DivisionByZeroException has appeared. There might not be comments to read yet!"

	if(RatioOfFillerToCanonWords >= 0.027 and RatioOfFillerToCanonComments >= 0.20):
		print "================================="
		print "Episode is classified as FILLER."
		print "================================="
		return class1
	else:
		print "=========================================="
		print "Episode is classified as NOT FILLER/CANON."
		print "=========================================="
		return class2


