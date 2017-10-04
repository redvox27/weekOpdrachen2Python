import operator

class Friendships:

    def __init__(self):
        self.friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
                       (3, 4), (4, 5), (5, 6), (5, 7), (6, 8),
                       (7, 8), (8, 9)
                       ]

        self.matrix = [[0 for self.x in range(10)] for self.y in range(10)]
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
                if self.matrix[i][j] > 0:
                    counter +=1

            counterList.append(counter)

        #counterList corrigeren:
        i = 1
        while i < len(counterList):
            counterList[i] -= 1
            i +=1

        i = 0
        while i < len(counterList):
            amountOfFriendsDict[i] = counterList[i]

            i+=1
        print(amountOfFriendsDict)

    def opgaveC(self):
        pass
f = Friendships()
f.opgaveA()
f.opgaveB()