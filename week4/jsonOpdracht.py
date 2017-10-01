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
                print(self.array[i]['title'])
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

        print(self.array)
        print(authorList)
        sortedAuthorList = (sorted(authorList))

        i = 0
        j = 0

        while i < len(sortedAuthorList):
            sortedTitle = sortedAuthorList[i]
            print("sorted title: ",sortedTitle)
            while j < len(self.array):
                print(self.array[j]['title'])
                j +=1

            i += 1

        return sortedBookList
b = BookReader('books.json')
print(b.getAveragePriceOfPythonBooks())
print(b.sortAuthors())