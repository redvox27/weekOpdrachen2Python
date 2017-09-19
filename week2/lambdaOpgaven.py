#opgave 6a
def removeDuplicatesFromList(array):
    tempList = []

    for element in array:
        if element not in tempList:
            tempList.append(element)

    return tempList

arr = [1,1,2,2,3,3,4,4,5,6,9,9,]

print(removeDuplicatesFromList(arr))

#opgave 6b
def getAllEvenElementsFromList(array):
    evenList = []

    for element in array:
        if element % 2 == 0:
            evenList.append(element)

    return evenList

print(getAllEvenElementsFromList(arr))

pangram = "The quick brown fox jumps over the lazy dog"

#opgave 6c
def isPangram(string):
    letterList = []

    string = string.replace(" ", "")

    for char in string:
        char = char.lower()
        if char not in letterList:
            letterList.append(char)

    if len(letterList) == 26:
        return True

    else:
        return False

print(isPangram(pangram))

#opgave 6d
