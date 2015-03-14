# SWE2015-Project
Private repo for Spring 2015 Software Engineering project

# Project Introduction
Crunchyroll (CR) is the leading platform for Japanese anime shows and Asian content. It delivers more than 25,000 episodes and over 15,000 hours of licensed media through their web application, mobile apps, and many other devices. The web application streams episodes for each show on CR and provides a communal viewing experience through a comments section where users leave short reviews related to an episode.

## 1.1 The problem
Despite Crunchyroll’s success in reaching over a million anime viewers, there is a general discontent with ‘filler’ content that is often present in anime. Filler episodes, or simply ‘fillers,’ are episodes that do not further plot and are irrelevant to the story; examples of fillers include flashback episodes, episodes that focus on a minor character or minor plot line, and unnecessarily long episodes. As an avid consumer of anime, I can attest to the community’s dislike for filler content, and the need for a way to avoid wasting time watching episodes that do not further the plot of the anime.

##1.2 A solution
I propose a project for the Option 2 track that classifies episodes streamed on Crunchyroll as either ‘filler’ or ‘not filler’ and ‘positive’ or ‘negative’. A third option of ‘neutral’ or ‘irrelevant’ will also be attributed to the comments if they are ambiguous or irrelevant to the episode. The classification will be done by performing a sentiment analysis on a sample of CR comments using a naïve Bayes classifier. This classifier will be trained using a dataset composed of 5,000 hand-classified Twitter tweets, which are similar to CR comments in terms of text length. The second classifier, which determines if an episode is a filler episode will also be a naïve Bayes classifier that uses the presence of words like ‘filler’ and ‘flashback’ as features.

In addition to the classification, the system will have a web interface in which users can see which shows on Crunchyroll are being tracked and their status (whether currently on filler content or not). The system will be a Django app which uses the Twilio service which users can text to find out the status of the latest episode for a tracked show. The idea is that the user will send a text message to the system’s number containing the name of the show they wish to know about, and the system will tell the user if their show’s latest episode is a filler episode or not.
