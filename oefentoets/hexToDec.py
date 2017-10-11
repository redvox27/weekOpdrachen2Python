hexaDecimal = "4F7A"
hexaDict = {"1" : 1, "2" : 2, "3" : 3, "4": 4, "5": 5, "6" : 6, "7": 7,
            "8" : 8, "9" : 9, "A" : 10, "B" : 11, "C" : 12, "D" : 13,
            "E" : 14,  "F": 15}

def convertHexToDec(hex):
    reversedHex = hex[::-1]
    i = 0
    power = 0
    decimalNumber = 0

    while i < len(reversedHex):
        hexCharacter = hexaDict[reversedHex[i]]
        decimalNumber += hexCharacter * 16** power

        power +=1
        i +=1
    print(decimalNumber)

convertHexToDec(hexaDecimal)