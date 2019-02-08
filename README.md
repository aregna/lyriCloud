## Lyricloud

A script that generates a word cloud from an artist's lyrics written in Python.

## Project Screen Shot(s)
![alt text](https://raw.githubusercontent.com/aregna/lyricloud/master/deathcabforcutie.png)
![alt text](https://raw.githubusercontent.com/aregna/lyricloud/master/elliottsmith.png)
![alt text](https://raw.githubusercontent.com/aregna/lyricloud/master/smashingpumpkins.png)
![alt text](https://raw.githubusercontent.com/aregna/lyricloud/master/froufrou.png)
![alt text](https://raw.githubusercontent.com/aregna/lyricloud/master/radiohead.png)
![alt text](https://raw.githubusercontent.com/aregna/lyricloud/master/frontbottoms.png)
![alt text](https://raw.githubusercontent.com/aregna/lyricloud/master/johnmayer.png)
![alt text](https://raw.githubusercontent.com/aregna/lyricloud/master/paramore.png)

## Installation and Setup Instructions

The dependencies for this project are those used in the following two libraries:
https://github.com/amueller/word_cloud
https://github.com/johnwmillr/LyricsGenius


## Reflection     
As a huge music fan I wanted to visualize common words in the lyrics of my favorite artists. Rather than reinventing the wheel, I looked into what technologies already existed to help me reach my end goal. The first is the Genius Lyrics wrapper and the second is a word cloud generator built by some talented people (see above!). I create a simple python dictionary that maps words in lyrics (from the genius api wrapper) to their frequency over the artists songs and then feed this into the word cloud generator code. I give the user options to input the arist and color scheme of their desire. 

#### Future Improvements:  
Now that I am in an Information Retrieval class, I'll be making some major updates to this project. Namely, instead of hardcoding a list of words I do not want to appear in my word clouds, I will find lists already compiled by others in the world of info retrival and linguistics. For example, what I called "filler words" in my script, can be replaced with a "stop words" dataset. I will also explore tokenization and other ways of visualizing the data. 
