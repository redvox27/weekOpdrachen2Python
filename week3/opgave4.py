class RomanLetterConverter():
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, romanString):
        decInt = 0

        #append de letters een voor een in de lijst
        romanLetterList = [letter for letter in romanString]

        print(romanLetterList)

        #er is 1 letter kan direct uit de dict gehaald worden
        if len(romanLetterList) == 1:
            decInt = self.rom_val.get(romanString)
            print(decInt)


        #deze check zorgt ervoor dat je niet twee keer aftrekt met I
        if len(romanLetterList) > 1:
            if romanLetterList[0] == 'I' and romanLetterList [1] == 'I':
                print("cant substract I twice: format has to be IX, IV etc")



        # kijk naar de volgorde van de romeinse letters
        #als een I voor een V komt dan moet je V - I doen

        #max maar 1 I kan je aftrekken van een heel getal


r = RomanLetterConverter()
r.romanToInt("IV")


