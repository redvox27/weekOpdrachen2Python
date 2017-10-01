from tkinter import *
from random import randint
import time

class Plotter():

    def __init__(self):
        self.running = True

        self.messageCounter = 1
        self.minValue = 0
        self.maxValue = 100

        self.s = 1
        self.x2 = 50
        self.y2 = self.value_to_y(randint(0, 100))

        self.root = Tk()
        self.root.title('simple plot')

        self.canvas = Canvas(self.root, width=1420, height=600, bg='white')  # 0,0 is top left corner
        self.canvas.pack(expand=YES, fill=BOTH)

        #buttons
        self.quitButton = Button(self.root, text='Quit', command=self.root.quit).pack()
        self.pauseButton = Button(self.root, text='Pause/Continue', command=self.pause).pack()
        self.subMitValues = Button(self.root, text='submitValue', command=self.getMinAndMaxValues).pack()
        #labels
        self.xLable = Label(self.root, text='x- as') #x-as lable
        self.xLable.place(x= 55, y=560)

        self.xLable = Label(self.root, text='x- as')# y-as lable
        self.xLable.place(x=15, y=460)

        self.minLable = Label(self.root, text= 'min value').place(x=945, y=603)
        self.maxLable = Label(self.root, text='max value').place(x=945, y=630)
        #tekstfields
        self.minValueEntry = Entry(self.root)
        self.minValueEntry.place(x=1000, y=603)

        self.maxValueEntry = Entry(self.root)
        self.maxValueEntry.place(x=1000, y=630)

        self.messageLog = Text(self.root)
        self.messageLog.place(x=1100, y=603)
        #lines

        self.canvas.create_line(50, 550, 1150, 550, width=2)  # x-axis
        self.canvas.create_line(50, 550, 50, 50, width=2)  # y-axis


        for i in range(23):
            x = 50 + (i * 50)
            self.canvas.create_line(x, 550, x, 50, width=1, dash=(2, 5))
            self.canvas.create_text(x, 550, text='%d' % (10 * i), anchor=N)

        # y-axis
        for i in range(11):
            y = 550 - (i * 50)
            self.canvas.create_line(50, y, 1150, y, width=1, dash=(2, 5))
            self.canvas.create_text(40, y, text='%d' % (10 * i), anchor=E)

    def value_to_y(self, val):
        return 550 - 5 * val

    def step(self):
        if self.running:
            if self.s == 23:
                self.s = 1
                self.x2 = 50

                self.canvas.delete("temp")

            x1 = self.x2
            y1 = self.y2
            self.x2 = 50 + self.s*50
            self.y2 = self.value_to_y(randint(self.minValue, self.maxValue))
            self.canvas.create_line(x1, y1, self.x2, self.y2, fill='blue', tags='temp')


            self.canvas.after(300, self.step)
            self.s += 1

    def pause(self):
        if self.running == True:

            self.running = False
        else:
            self.running = True

        self.step()
        print(self.running)

    def getMinAndMaxValues(self):
        if self.minValueEntry.get() == '' or self.maxValueEntry.get() == '':
            self.messageLog.insert(INSERT, str(self.messageCounter) + ' :enter values in both fields \n')
            self.messageCounter +=1
        else:

            minValue = int(self.minValueEntry.get())
            maxValue = int(self.maxValueEntry.get())

            # self.canvas.create_line(50, 550, 1150, 550, width=2)  # x-axis
            # self.canvas.create_line(50, 550, 50, 50, width=2)  # y-axis

            #minValueLine = self.canvas.create_line(50, 550, minValue, 550)
            if minValue > maxValue:

                self.messageLog.insert(INSERT, str(self.messageCounter) + ' :minValue has to be smaller than max \n')
                self.messageCounter += 1

            else:
                self.minValue = minValue
                self.maxValue = maxValue
                #self.canvas.place(minValueLine)





    def main(self):
        self.canvas.after(300, self.step)
        self.root.mainloop()
p = Plotter()
p.main()