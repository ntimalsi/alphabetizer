#!/usr/bin/env python3

def alphabetizer(givenString: str) -> str:
    """
     Using Python's sorted function to sort the result. Thus, Time Complexity is O(nLogn) due to Tim Sort
    Args:
    givenString (str): The string to test

    Returns:
    finalString (str): The alphabetized string
    """
    sortString = sorted(givenString, key=str.lower) 
    finalString=""
    if not givenString:
        return ""

    for string in sortString:
        if not string.isalpha():
            continue
        finalString+= string
    return finalString

if __name__ == '__main__':
    try:
        while True:
            tester = input("Enter a string to alphabetize or press Ctrl+C to interrupt:")
            print(alphabetizer(tester))

    except (KeyboardInterrupt):
        print("Interrupted")
    finally:
        print("\nClosed")