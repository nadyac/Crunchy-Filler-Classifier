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

'''
----------------------------------------------------------------------------
classifyFillerOrCanon - takes in a new episode's comments and its corresponding
	prior probability of a filler and returns a Class = {Filler, NotFiller/Canon, Unknown}
	
	NOTE 1: Currently prior probability is set to 0.25 which was an average calculated
	from a small sample of 20 shows. Of those 20 shows, 20,000 comments were extracted
	to get the features of filler episodes used in this classifier.

	NOTE 2: Currently, it is not performing a Naive Bayes because I need to create
	and clean a dataset for Non-Filler episodes. Due to time constraints, this 
	is not feasible at the moment. For the time being, the classifier uses the 
	two features extracted from the sample of filler episode comments to classify.

	NOTE 3: Classifier seems to perform well, even without the Naive Bayes.

Inputs: 
- probabilityOfFiller: (float), Probability of the given show having a filler episode
- document: list of comments for the new episode

Outputs: 
- Class = {Filler, NoFiller/Canon, Unknown}

Variables:
- class0: String, identifies the 'unknown' class 
- class1: String, identifies the 'Filler' class 
- class2: String, identifies the 'NotFiller/Canon' class 
- RatioOfFillerComments: Float, filler comments / total comments 
- RatioOfFillerWords: Float, filler words / total words
- commentsCount: int, total comments in the new episode
- fillerCount: int, total count of filler words (recap, flashback, filler)
- wordCount: int, total word count in the document
- commentsWithFillerWords: int, comments that contain at least 1 filler word 
----------------------------------------------------------------------------
'''
def classifyFillerOrCanon(probabilityOfFiller, document):

	class0 = 'Unknown'
	class1 = 'Filler'
	class2 = 'Not Filler'
	RatioOfFillerComments = 0
	RatioOfFillerWords = 0

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

	print "Total comments: " + str(commentsCount)
	print "Total comments with filler words " + str(commentsWithFillerWords)

	try:
		RatioOfFillerComments = (commentsWithFillerWords)/(commentsCount)
		RatioOfFillerWords = (fillerCount)/(wordCount)
		print "Ratio of filler comments: " + str(RatioOfFillerComments)
		print "Ratio of filler words: " + str(RatioOfFillerWords)
	except ZeroDivisionError as e:
		print "A wild DivisionByZeroException has appeared. There might not be comments to read yet!"
		print "================================="
		print "Episode is classified as UNKNOWN."
		print "================================="
		return class0
	if(RatioOfFillerWords >= 0.027 and RatioOfFillerComments >= 0.20):
		print "================================="
		print "Episode is classified as FILLER."
		print "================================="
		return class1
	else:
		print "=========================================="
		print "Episode is classified as NOT FILLER/CANON."
		print "=========================================="
		return class2


