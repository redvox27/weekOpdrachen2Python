class Stack:

    def __init__(self):
        self.elementList = []

    def isEmpty(self):
        if len(self.elementList) == 0:
            return True

        else:
            return False

    def peek(self):

        if not self.isEmpty():
            topOfStack = self.elementList[len(self.elementList)-1]
            return topOfStack

    def push(self, value):
        self.elementList.append(value)

    def pop(self):
        if not self.isEmpty():
            topOfStack = self.elementList[len(self.elementList)-1]
            self.elementList.remove(self.elementList[len(self.elementList)-1])
            return topOfStack


    def getSize(self):
        size = len(self.elementList)
        return size

stack = Stack()
for i in range(10):
    stack.push(i)

while not stack.isEmpty():
# prints 9 8 7 6 5 4 3 2 1 0
    print(stack.pop(), end = " ")
