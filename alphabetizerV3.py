#!/usr/bin/env python3
from collections import Counter


def alphabetizer(givenString: str) -> str:
    """
    For this approach, I made use of the Counter module from collections package.
    First, I initialized a list with alphabets, then passed the given string to Counter class
    which returns a dictionary with count of the letters. This is a clean approach. Concise code with time complexity O(N)

    Args:
    givenString (str): The string to test

    Returns:
    finalString (str): The alphabetized string
    """

    if not givenString:
        return ""
    finalString=""
    alphas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
        , 'u', 'v', 'w', 'x', 'y', 'z'
              ]
    #Counting frequency of each letter e.g {l:1,e:2 }
    counts = Counter(givenString)

    for i in alphas:
        #Checking if alphabet exists in the given string
        if i in givenString:
            #appending the character according to its frequency
            finalString+=counts[i] * i
            #Checking if the same letter appears in uppercase
        if i.upper() in givenString:
            finalString+=counts[i.upper()] * i.upper()

    return  finalString

if  __name__ == '__main__':
    try:
        while True:
            tester = input("Enter a string to alphabetize or press Ctrl+C to interrupt:")
            print(alphabetizer(tester))

    except (KeyboardInterrupt):
        print("Interrupted")
    finally:
        print("\nClosed")


