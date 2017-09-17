from math import isclose
class PerfectNumberChecker():
    perfectNumberList = []

    def fillPerfectNumberList(self):
        candidateNumber = 1

        while candidateNumber < 10000:
            self.perfectNumberCheck(candidateNumber)

            candidateNumber += 1

    def printPerfectNumberList(self):
        print(self.perfectNumberList)

    def perfectNumberCheck(self, checkNumber):
        numberList = []
        i = 1

        while i < checkNumber:
            result = checkNumber / i

            if self.isWhole(result):
                numberList.append(i)

            if(sum(numberList) > checkNumber):
                break
            i += 1

        if(sum(numberList) == checkNumber):
            self.perfectNumberList.append(checkNumber)
            print("perfectNumber Found")


    def isWhole(self, number):
        if (number % 1 == 0):
            return True

        else:
            return False


p = PerfectNumberChecker()
#p.perfectNumberCheck(28)
p.fillPerfectNumberList()
p.printPerfectNumberList()
