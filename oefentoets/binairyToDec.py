binairyString = "1110"

def binaryToDec(string):
    reverseString = string[::-1]
    index = 0
    power = 0
    decNumber = 0

    while index < len(reverseString):
        if int(reverseString[index]) == 1:
            decNumber += 2**power

        index +=1
        power +=1

    print(decNumber)
binaryToDec(binairyString)