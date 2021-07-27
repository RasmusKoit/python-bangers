"""
Couple of examples of previous lesson
"""

from typing import *

def firstLetter(word: str) -> str:
    """

    Args:
        word (str): input word

    Returns:
        [str]: [Returns a string with single character]
    """
    return word[0]


def createStrList(longString: str, delimiter=' ') -> List:
    """

    Args:
        longString (str): long string
        delimiter (str, optional): what do you want to seperate your string with. Defaults to ' '.

    Returns:
        List
    """
    return longString.split(delimiter)


def printWords(words: List):
    for word in words:
        print(word)



if __name__ == '__main__':
    inputText = "I like to ride my car super fast, I own 3 cars and they are called: Bugatti, Honda and Jaguar"

    myTextList = createStrList(inputText)
    
    # Lets print out our words from the list
    printWords(myTextList)
    
    # Lets print out each words first character
    for element in myTextList:
        print(firstLetter(element))
        

