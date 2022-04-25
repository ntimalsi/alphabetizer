#!/usr/bin/env python3

def alphabetizer(givenString: str) -> str:
    """
    Since the output contains alphabetic characters and there are 26 alphabetic characters,
    I decided to store the frequency of lowercase and uppercase letters and then sort them. This approach gives O(N) time complexity.
    Args:
    givenString (str): The string to test

    Returns:
    finalString (str): The alphabetized string
    """
    if isinstance(givenString,str) is False or len(givenString) == 0:
        return ""
        
    alphaFreqMap = [] 
    for _ in range(26):
        alphaFreqMap.append([0,0]) #alphaFreqMap holds the frequency of lower case and uppercase letters from the given string
        
    for character in givenString:
        ascii_value = ord(character)
        if (ascii_value >= 65 and ascii_value <= 90) or (ascii_value >= 97 and ascii_value <= 122):
            if (ascii_value >= 97 and ascii_value <= 122):  
                alphaFreqMap[ascii_value-97][0] += 1 #lowercase
            else:                                         
                alphaFreqMap[ascii_value-65][1] += 1 #uppercase
    alphabatically_sorted_str = ""
    index = 0
    for alphabet in alphaFreqMap:    
        if alphabet[0] != 0:     
            alphabatically_sorted_str += alphabet[0] * chr(97+index)
        if alphabet[1] != 0:     
            alphabatically_sorted_str += alphabet[1] * chr(65+index)
        index += 1
    return alphabatically_sorted_str


if __name__ == '__main__':
    try:
        while True:
            tester = input("Enter a string to alphabetize or press Ctrl+C to interrupt:")
            print(alphabetizer(tester))

    except (KeyboardInterrupt):
        print("Interrupted")
    finally:
        print("\nClosed")
