# # Word Frequency
# ## Directions
# In this project, you will use `open` to read in a text file and calculate the frequency of words in that file.
# To calculate the frequency of words, you must:
# - remove punctuation
#   +Define what counts as "punctuation"
#   +Loop throough all of the lines of text to identify and remove any punctuation
# - normalize all words to lowercase
#   +Loop through the lines in the text string to identify any upper case characters, and change them to lower case
# - remove "stop words" -- words used so frequently they are ignored
#   +Convert the text file string into a list - parse out the words based on spaces(?)
#   +Use the STOP_WORDS list to filter out from the file or the word count
# - go through the file word by word and keep a count of how often each word is used:
#   +Iterate over the list to create a dictionary(?)
#   +Count each word in the file & display a list of every word and the number of times it was used.
#   +Add code to print the list in the terminal
#   +Be able to use commands in terminal to access/view the printed info
#
# When your program is complete, you should be able to run 
# ```
# python3 word_frequency.py praise_song_for_the_day.txt
# ``` 
# and get a printed report like this:
# ```
#      we | 7 *******
#    each | 5 *****
#      or | 5 *****
#    need | 5 *****
#    love | 5 *****
#   about | 4 ****
#  praise | 4 ****
#    song | 4 ****
#     day | 3 ***
#     our | 3 ***
# ```
# ## Starter Files
# A starting program is located in `word_frequency.py`.
# ## Resources
# - [The `dict` type in Python 3](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
# - [f-strings in Python 3](https://realpython.com/python-f-strings/)
# ### Bibliography
# - [Elizabeth Alexander, _Praise Song for the Day_](https://www.poetryfoundation.org/poems/52141/praise-song-for-the-day)
# - [Richard Blanco, _One Today_](https://poets.org/poem/one-today)
# - [Amanda Gorman, _The Hill We Climb_](https://en.wikipedia.org/wiki/The_Hill_We_Climb)

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

#Import regex library
import re
# def word_count(file):

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as file:
        # Return all lines in the file, as a list where each line is an item in the list object
        # lines = text.readlines()
        """Return all lines in `file` as a list where the entire text string is a list object."""
        lines = file.read()
        print(f"{len(lines)} lines in the file.")
        words = lines.split()
        # print(lines)

        #Using a regex sub-string function, find all of the punctuation in our variable (line) and replace it with nothing
            # re.sub(pattern, replacement, original_string)
            # because of the use of backslashes in regex, add an "r" before the pattern and wrap the pattern in quotes to convey that the code should look at the raw string
            # the regex combo to find all punctuation includes: "^" to mean "not" + 
            # "\w" to match alphanumeric characters (ie class: [a-zA-Z0-9_]) and "\s" to match any whitespace character (ie class: [ \t\r\f\v])
            # r'[^\w\s] = for any character in the raw string that is NOT alphanumeric or a whitespace character
            # add the .lower method to the end of the sub-string function to convert all text to lowercase
        for word in words:
            word = re.sub(r'[^\w\s]','',word).lower()
            word = word.replace('\n', '')
        print(words)


            # word_list = list(line)
            # print (word_list)
        # word_list = list(lines) not in STOP_WORDS
        # print(word_list)
            # for words in line:
        # words = lines.split(" ")
        # print(words)
            # words.join()?
            #how do I combine all of the words?
# Alt method for removing punctuation:
    # for line in lines:
    #     line = line.replace(",", "")
    #     line = line.replace(".", "")
    ##Repeat this function for all of the different punctuation types, followed by:
    #     line = line.lower()
    """Map the words (dict) other than the list (STOP_WORDS[::]).  key = string(word) : value = word count(+=)"""
    #remove_from_list(list, STOP_WORDS)



# This tells the script where to look to run the code
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

"""this calls the file to run"""
file = Path(args.file)
if file.is_file():
    print_word_freq(file)
else:
    print(f"{file} does not exist!")
    exit(1)
