class WeatherStation():
    file = open("station_vl.txt", "r")
    testList = []
    hourList =[]
    dayList = []
    temperatureList = []


    def getFile(self):
        return self.file

    def makeListOfFile(self):
        self.testList = (self.getFile().read().strip().split())
        print(self.testList)

    def cleanTestList(self):
        self.testList = self.testList[6:]
        print(self.testList)

    def fillLists(self):
        i = 0
        testList = self.testList

        while i < len(self.testList ) -3:
            day = testList[i]
            hour = testList[i+1]
            temperature = testList[i +2]

            #print("day: ", day, "hour: ", hour, "temperature: ", temperature)
            self.dayList.append(int(day))
            self.hourList.append(int(hour))
            self.temperatureList.append(int(temperature))
            i += 3

    def getAverageTemperature(self):
        sumOfList = sum(self.temperatureList)
        lengthOfList = len(self.temperatureList)
        average = sumOfList / lengthOfList
        print(average)

w = WeatherStation()
w.makeListOfFile()
w.cleanTestList()
w.fillLists()
w.getAverageTemperature()
#TODO print gemiddelde temperaturen
#TODO print gemiddelde temeratuur per dag