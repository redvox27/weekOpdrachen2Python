#http://www.tuxx.nl/romeinse_cijfers/
#https://educatie-en-school.infonu.nl/buitenlands/11686-romeinse-cijfers-tabel-uitleg.html

class RomanLetterConverter():
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    combinationList = ("IV", "IX", "XL", "XC", "CD", "CM")
    decInt = 0

    def romanToInt(self, romanString):

        #append de letters een voor een in de lijst
        romanLetterList = [letter for letter in romanString]
        loopedLetters = []

        print(romanLetterList)

        #er is 1 letter kan direct uit de dict gehaald worden
        if len(romanLetterList) == 1:
            self.decInt = self.oneDigitCheck(romanString)

        if len(romanLetterList) == 2:
            self.decInt = self.twoDigitCheck(romanLetterList)

        #hier kan ik per 2 kijken
        if len(romanLetterList) > 2:
            i = 0
            while i < len(romanLetterList) -1:
                firstLetter = self.rom_val.get(romanLetterList[i])
                secondLetter = self.rom_val.get(romanLetterList[i+1])

                #Getal mag alleen worden afgetrokken als eerste getal kleiner is dan voorste
                if firstLetter > secondLetter:
                    self.decInt += firstLetter
                    i+=1

                #Kleinere getal mag worden afgetrokken van grotere getal
                elif firstLetter < secondLetter:
                    self.decInt += (secondLetter - firstLetter)
                    i += 2

                elif firstLetter == secondLetter:
                    j = i + 1
                    startValue = i
                    sameLetterCounter = 2
                    while j < len(romanLetterList) -1:
                        if romanLetterList[j] == romanLetterList[j+1]:
                            sameLetterCounter +=1
                            loopedLetters.append(romanLetterList[j])
                            j +=1

                        else:
                            break

                    self.decInt += self.rom_val.get(romanLetterList[startValue]) * sameLetterCounter

                    i += sameLetterCounter
            print(i)
            print(len(romanLetterList))
            if i == len(romanLetterList) -1:
                self.decInt += self.rom_val.get(romanLetterList[len(romanLetterList)-1])

    def oneDigitCheck(self, romanString):
        decInt = self.rom_val.get(romanString)
        return decInt

    def twoDigitCheck(self, romanLetterList):
        firstLetter = self.rom_val.get(romanLetterList[0])
        secondLetter = self.rom_val.get(romanLetterList[1])

        romanString = romanLetterList[0] + romanLetterList[1]

        if firstLetter == secondLetter:
            decInt = firstLetter + secondLetter
            return decInt

        elif firstLetter < secondLetter:
            if romanString in self.combinationList:
                decInt = secondLetter - firstLetter
                return decInt

            else:
                print("wrong combination: only IV, IX, XL, XC, CD and CM are allowed")
        else:
            decInt = secondLetter + firstLetter
            return decInt

    def printDecNumber(self):
        if self.decInt:
            print(self.decInt)

r = RomanLetterConverter()
r.romanToInt("XXX")
r.printDecNumber()


