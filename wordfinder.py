"""Word Finder: finds random words from a dictionary."""

import random 

class WordFinder:
    """ Finds random words from a dictionary

    >>> wf = WordFinder("words.txt")
    There are 235886 words in the dictionary

    >>> wf.random()
    'epithalamus'

    >>> wf.random()
    'trapezia'

    >>> wf.random()
    'zoosperm'

    >>> wf.random()
    'wheatear'
    
    """
    def __init__(self,file):
        """ reads a dictionary and prints how many words are in the file"""

        dictionary = open(file,'r')
    
        self.word = self.lines_of_dict(dictionary)

        print(f'There are {len(self.word)} words in the dictionary')
        print(f'{self.word}')

    def lines_of_dict(self, dictionary):
        
        return [word.strip() for word in dictionary]
    
    def random_word(self):
        "returns a random word"

        return random.choice(self.word)
    
class SpecialWordFinder(WordFinder):
    """ Find words while avoiding blank lines and lines that start with "#" 
        
    >>> swf = WordFinder("other_words.txt")
    3 words read

    >>> swf.random()
    'kale'

    >>> swf.random()
    'apple'

    >>> swf.random()
    'mango'

    >>> swf.random()
    'parsnips'
    
    
    """
    def __init__(self,file):
        super().__init__(file)

    def lines_of_dict(self,dictionary):
        return [word.strip() for word in dictionary if word.strip() and not word.startswith("#")]