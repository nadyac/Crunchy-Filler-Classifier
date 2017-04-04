# The Crunchy Filler Notifier
Imagine this: you've waited all week for a new episode of your favorite show to come out. You've told everyone how good this show is and how you can't wait to tune in as soon as the broadcast starts. So you do that, and to your disappointment, it's a recap episode. Nothing new, just filler. Your heart sinks and you can't help but feel like you've wasted your time. Unfortunately, some shows do this to their viewers quite often.
But wait. What if there were some way for you to know if the latest episode of your favorite show is worth your time or not? Read on.

### What is this?
Crunchy Filler Notifier (CFN) is a system that notifies users if a show on Crunchyroll released a filler episode recently. A <b>filler episode</b> is an episode that has repetitive or irrelevant content and does not advance the plot of the show. Examples of fillers are flashback episodes, recaps, or episodes where nothing new happens, old scenes are reused, and viewers are left with an uncomfortable feeling of disatisfaction. 
Crunchy Filler Notifier can help users by automatically classifying episodes as "Filler" or "Canon"( not filler). 

### How?
It does this by visiting the Crunchyroll site, going to a show's page, and extracting the comments for the latest episode.
It then processes the comments and performs a Naive Bayes classification to determine if an episode is more likely to be a
filler episode or not. Then it sends you back the results.

### What do I need to run this project on my machine?
This project requires <b>Python 2.7</b> (though currently upgrading to 3.6), <b>Selenium</b>, <b>Mechanize</b> (currenty upgrading to RoboBrowser), and <b>Flask</b> in order to run. If you have pip installed then obtaining all the necessary components is only a matter of running "pip install Selenium", "pip install RoboBrowser", and "pip install Flask" in your terminal.

#### Homepage
#### ==========
<img src="http://i.imgur.com/kmUN2OW.png"></img>

#### Shows page
#### ===========
<img src="http://i.imgur.com/N3S76iB.png"></img>

#### Episodes Page
#### ==============
<img src="http://i.imgur.com/MlDME2G.png"></img>
