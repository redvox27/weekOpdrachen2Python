import  time
class Stopwatch():


    def __init__(self):
        self.startTime = time.clock()
        self.stopTime = 0

    def start(self):
        self.startTime = time.clock()
        return self.startTime

    def stop(self):
        self.stopTime = time.clock()
        return self.stopTime

    def getElapsedTime(self):
        elapsedTime = self.stopTime - self.startTime
        return elapsedTime

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        if self.stopTime > 0:
            return self.stopTime

        else:
            print("no stoptime measured")

size = 10000000
stopWatch = Stopwatch()
sum = 0
for i in range(1, size + 1):
    sum += i
stopWatch.stop()

print("The loop time is", stopWatch.getElapsedTime(), "milliseconds")
