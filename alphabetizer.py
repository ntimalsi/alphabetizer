tester = "3 Blind Mice"

def alphabetizer(givenString):
    sortString = sorted(givenString, key=str.lower)
    finalString=""
    for string in sortString:
        if not string.isalpha():
            continue
        finalString+= string
    return finalString


print(alphabetizer(tester))
