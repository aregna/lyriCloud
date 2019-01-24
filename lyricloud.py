'''
Lyricloud is a small script that generates a word cloud for an artist given by user input.
I use a genius lyrics wrapper created by @johnwmillr (https://github.com/johnwmillr/LyricsGenius)
and a word cloud library created by @kavgan (https://github.com/kavgan/word_cloud).
I first gather the data from the wrapper, clean it, get a count_frequency
count and then pass it to the word cloud generator.
'''

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import lyricsgenius as genius
import json
import re

api = genius.Genius('F4d9Q4MdZrHM1E9S6krWVMy1VdSUtJPc8Hqir_WF8GxQd5P8iK1C65EvQx2Vp1O6') #edit out
word_dict = {} # a hash map of words and their frequencies
colors = {"1": "Reds", "2": "Oranges", "3": "Greens", "4": "Blues",
          "5": "Purples", "6": "Greys"}


def main():
    # get artist song data & save in a json file
    query = input("Who is the artist you want to generate a word cloud from? ")
    artist = get_artist(query)
    artist.save_lyrics(format='json')
    query_format = re.sub(r'[ ]', "", query)
    artist_data = get_json('./Lyrics_'+ query_format + '.json')

    # add words and frequencies to wordDict to generate word cloud
    for i in range(len(artist_data['songs'])):
        parse_lyrics(artist_data['songs'][i]['lyrics'])

    create_cloud(query, word_dict)

# access JSON file
def get_json(file_path_name):
    """ loads in a json file and returns a json object

    Args:
        file_path_name: the location of the json file

    """
    with open(file_path_name, 'r', encoding='utf-8') as fp:
        return json.load(fp)


def keep_word(word):
    """ Determines if a word should be included in the word cloud; must be longer than 4 letters and not a generic word

    Args:
        word: the word/lyric we are deciding to keep or omit from the word cloud

    Returns:
        Returns true if the word should be included in the word cloud, otherwise returns false.

    """
    remove_words = ["chorus", "refrain", "verse", "intro", "bridge", "hook",
                   "prechorus", "outro", "yeah", "it's", "that", "there",
                   "then", "when","who", "what", "like", "you're", "your",
                   "from", "where", "don't", "won't", "can't", "we're", "we'll",
                   "that's", "gonna", "wanna", "could", "would", "these", "those",
                   "ain't", "aint", "'cause", "cause"]
    if word in remove_words or len(word) <= 4:
        return False
    return True


# update word frequency across all songs
def count_frequency(word_arr):
    """ Populates a word frequency dictionary for each word that is to be included in the word cloud

    Args:
        word_arr: The array of words in the lyrics of an artist's music

    """
    for word in word_arr:
        if keep_word(word.lower()):
            if word.lower() in word_dict:
                word_dict[word.lower()] += 1
            else:
                word_dict[word.lower()] = 1


# parse lyrics from one song by white space
def parse_lyrics(lyrics):
    """ Cleans lyric format from characters outside of a-Z, apostraphe, space or new line and then
        reformats all words to be split on a single white space character

    Args:
        lyrics: The lyrics of an artist's music.

    """
    lyrics = re.sub(r'[^A-Za-z\' \n]', "", lyrics) # deletes everything that's not a-Z, ', space or newline
    lyrics = re.sub(r'[\n]', " ", lyrics)          # replaces \n with space
    words = lyrics.split(" ")
    count_frequency(words)


def get_artist(query):
    """ Attempts to get user input from Lyrics Genius

    Args:
        query: The query from the user of what artist they want to generate a word cloud from

    Returns:
        The data associated with the artist queried from the genius lyrics api wrapper

    """
    try:
        query_data = api.search_artist(query, max_songs=50)
    except AssertionError:
        print("This artist is not on Genius Lyrics. Please check your spelling,"
              "or try another artist.\n")
    return query_data


def get_color():
    """ Asks the user for input on what color scheme they want their word cloud to be

    Returns:
        The color scheme desired by the user

    """
    query_color = input("Type the number of the color you want:\n 1: Red\n"
                  " 2: Orange\n 3: Green\n 4: Blue\n 5: Purple\n 6: Grey\n")
    while(query_color not in colors):
        query_color = input("Type the number of the color you want:\n 1: Red\n"
                      " 2: Orange\n 3: Green\n 4: Blue\n 5: Purple\n 6: Grey\n")
    return colors[query_color]


def create_cloud(query, word_data):
    """Creates the lyric cloud for the artist given the data that was cleaned and counted

    Args:
        query: The artists name inputted by the user
        word_data: The frequency data of words by the artist

    Returns:
        The return value. True for success, False otherwise.

    """
    wc = WordCloud(max_words=1000, background_color='black',
                   colormap= get_color()).generate_from_frequencies(word_data)
    plt.title(query + " Word Cloud")
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    wc.to_file("word_cloud_" + query + ".png")

main()
