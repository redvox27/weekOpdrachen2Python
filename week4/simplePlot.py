from tkinter import *
from random import randint
import time

class Plotter():

    def __init__(self):
        self.running = True

        self.s = 1
        self.x2 = 50
        self.y2 = self.value_to_y(randint(0, 100))

        self.root = Tk()
        self.root.title('simple plot')

        self.canvas = Canvas(self.root, width=1200, height=600, bg='white')  # 0,0 is top left corner
        self.canvas.pack(expand=YES, fill=BOTH)

        self.quitButton = Button(self.root, text='Quit', command=self.root.quit).pack()
        self.pauseButton = Button(self.root, text='Pause/Continue', command=self.pause).pack()

        self.xLable = Label(self.root, text='x- as') #x-as lable
        self.xLable.place(x= 55, y=560)

        self.xLable = Label(self.root, text='x- as')# y-as lable
        self.xLable.place(x=15, y=460)

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
            self.y2 = self.value_to_y(randint(0, 100))
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
    def main(self):
        self.canvas.after(300, self.step)
        self.root.mainloop()
p = Plotter()
p.main()