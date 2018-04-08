import sys
import collections
import string

def mostCommonWords(file, top=10):    
    ''' Returns the most common words in a file.'''
    words = collections.Counter()
    with open(file) as file:
         for line in file:
              words.update(sanitizeLine(line))
    return dict(words.most_common(top))

def wordCount(file):
    '''Returns the wordcount of a file.'''
    total_words = 0
    with open(file) as file:
        for line in file:
            total_words += len(sanitizeLine(line))
    return total_words

def sanitizeLine(line):
    '''converts a string of words into an array of words in lowercase and without punctuation'''
    return line.lower().translate(None, string.punctuation).split()


if __name__ == '__main__':
    file = sys.argv[1]
    wordCount = wordCount(file)
    commonWords = mostCommonWords(file)
    print("Running wordCount and mostCommonWords on {}".format(file))
    print("Word Count: {}".format(wordCount))
    print("Top 10 Common words: {}".format(commonWords))