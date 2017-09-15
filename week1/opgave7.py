def opgave7(woord):

    i = 0

    while i < len(woord):

        #TODO gebruik slicing [::-1] deze statement draait het woord om
        firstCheckLetter = woord[i]
        secondCheckLetter = woord[len(woord) - i -1]
        print("second: ", secondCheckLetter)
        print("first: ",firstCheckLetter)
        if firstCheckLetter == secondCheckLetter:

            i += 1
        else:
            print("geen palindroom")
            break
    if(i == len(woord)):
        print("palindroom found")
opgave7("malayalam")

def opgave7Better(woord):
    mirror = woord[::-1]

    if woord == mirror:
        print("palindroom found")
    else:
        print("no palindroom found")

opgave7Better("lepels")
