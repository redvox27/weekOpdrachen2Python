import operator
import numpy as np
class Friendships:
    interests = [
        (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0,
                                                                                  "Storm"), (0, "Cassandra"),
        (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
        (2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"),
        (2, "pandas"), (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
        (4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"),
        (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programminglanguages"),
        (6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"),
        (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"),
        (8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificialintelligence"),
        (9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")
    ]
    def __init__(self):
        self.friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
                       (3, 4), (4, 5), (5, 6), (5, 7), (6, 8),
                       (7, 8), (8, 9)
                       ]

        self.matrix = [['x' for self.x in range(10)] for self.y in range(10)]
        self.matrix[9][0] = 9

    def opgaveA(self):
        i = 0
        while i < len(self.friendships):
            person = self.friendships[i][0]
            friend = self.friendships[i][1]

            # set persoon op default plaats
            self.matrix[person][0] = person

            # set vriend op juiste plaats
            self.matrix[person][friend] = friend

            # het omgekeerde van voren moet geset worden anders klopt het niet meer
            if i < 7:
                self.matrix[friend][person+1] = person
            else:
                self.matrix[friend][person] = person

            i += 1
        self.printRows()

    def printRows(self):
        for row in self.matrix:
            print(row)

    def opgaveB(self):
        counterList = []
        amountOfFriendsDict = {}

        #counterList vullen met aantal vrienden per persoon
        for i in range(0, len(self.matrix)):
            counter = 0
            for j in range(0, len(self.matrix)):
                if self.matrix[i][j] != 'x':
                    counter +=1

            counterList.append(counter)

        #counterList corrigeren:
        i = 1
        while i < len(counterList):
            counterList[i] -= 1
            i +=1

        #dictionary maken
        i = 0
        while i < len(counterList):
            amountOfFriendsDict[i] = counterList[i]

            i+=1
        print(amountOfFriendsDict)

    def opgaveC(self, firstPersonIndex, secondPersonIndex):
        firstFriendList = []
        secondFriendList = []
        matchList = []


        for i in range(1, len(self.matrix)):
            if self.matrix[firstPersonIndex][i] != 'x':
                firstFriendList.append(self.matrix[firstPersonIndex][i])

        for i in range(1, len(self.matrix)):
            if self.matrix[secondPersonIndex][i] != 'x':
                secondFriendList.append(self.matrix[secondPersonIndex][i])

        for friend in firstFriendList:
            if friend in secondFriendList:
                matchList.append(friend)


        print(matchList)

    def opgaveD(self):
        interestDict =self.fillDictD_E()

        i = 0
        while i < len(self.interests):
            person = self.interests[i][0]
            print(self.interests[i][1])

            interestDict[person].append(self.interests[i][1])
            i +=1

        print(interestDict)

    def fillDictD_E(self):
        tempDict = {}
        i = 0
        while i < len(self.interests):
            tempDict[i] = []
            i +=1

        return tempDict

    def opgaveE(self):
        bookDict = {}
        i = 0
        while i < len(self.interests):
            bookDict[self.interests[i][1]] = []
            i +=1

        i =0
        while i < len(self.interests):
            book = self.interests[i][1]

            bookDict[book].append(self.interests[i][0])

            i +=1

        print(bookDict)

f = Friendships()
#f.opgaveA()
#f.opgaveB()
#f.opgaveC(2, 1)
#f.opgaveD()
f.opgaveE()