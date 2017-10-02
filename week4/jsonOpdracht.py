import json

class BookReader():

    def __init__(self, jsonFile):
        self.jsonData = open(jsonFile)
        self.array = json.load(self.jsonData)


    def getArray(self):
        return self.array

    def getAveragePriceOfPythonBooks(self):
        i = 0
        bookCounter = 0
        price = 0
        while i < len(self.array):
            if "Python" in self.array[i]['title']:
                price += self.array[i]['price']
                bookCounter +=1
                i +=1
            i +=1

        return (price / bookCounter)

    def sortAuthors(self):
        i = 0
        authorList = []
        sortedBookList = []
        while i < len(self.array):
            authorList.append(self.array[i]['author'])
            i += 1

        sortedAuthorList = (sorted(authorList))

        for i in range(len(sortedAuthorList)-1):
            sortedTitle = sortedAuthorList[i]
            for j in range(len(self.array) -1):
                arrayTitle = self.array[j]['author']

                if sortedTitle == arrayTitle:
                    sortedBookList.append(self.array[j])
                    del self.array[j]

        return sortedBookList
b = BookReader('books.json')
print(b.getAveragePriceOfPythonBooks())
print(b.sortAuthors())