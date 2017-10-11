# convert an integer to a hex digit (a character)
def hex_char(value):
    if value <= 9 and value >= 0:
        return chr(value + ord('0'))
    else:
        return chr(value - 10 + ord('A'))


# convert a decimal to a hex as a string
def to_hex(decimal):
    remainderList = []
    while decimal > 0:
        remainder = decimal % 16
        result = decimal // 16
        remainderList.append(remainder)
        decimal = result
    return remainderList[::-1]

def main():
    inputDec = int(input("vul decimaal in"))

    remainderList = to_hex(inputDec)
    hexaDecimal = ""
    for remainder in remainderList:
        hexaDecimal += hex_char(remainder)

    print(inputDec)


main()
