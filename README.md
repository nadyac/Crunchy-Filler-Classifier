# The Crunchy Filler Notifier

### What?
This system notifies users if a show on Crunchyroll released a filler episode recently
### How?
It does this by visiting the Crunchyroll site, going to a show's page, and extracting the comments for the latest episode.
It then processes the comments and performs a Naive Bayes classification to determine if an episode is more likely to be a
filler episode or not. Then it sends you back the results.
### What do I need to run this project on my machine?
This project requires <b>Python 2.7</b>, <b>Selenium</b>, <b>Mechanize</b>, and <b>Flask</b> in order to run. If you have pip installed then obtaining all the necessary components is only a matter of running "pip install Selenium", "pip install Mechanize", and "pip install Flask" in your terminal.

This is my Spring 2015 Software Engineering project.

#### Homepage
####=========
<img src="http://i.imgur.com/kmUN2OW.png"></img>


