def opgave7(woord):

    i = 0

    while i < len(woord):
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