from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from collections import Counter
import operator
import itertools
def show_result():
    analyze_file(filename.get())


def analyze_file(filename):
    try:
        infile = open(filename, "r")
        counts = Counter()
        wordArray = []
        frequencyArray = []

        for word in infile.read().split('.'):
            if len(word) > 1:
                counts[word] +=1

        # your code
        print(counts)
        #vul frequency list op een gesorteerde manier
        for value in sorted(counts.values(), reverse=True):
            frequencyArray.append(value)

        #pak tien meest volkomende frequencies
        frequencyArray = frequencyArray[:10]

        #append de tien woorden met de hoogste frequentie in woordArray
        i = 0
        while i < 11:
            wordArray.append(max(counts.items(), key=operator.itemgetter(1))[0])
            del counts[max(counts.items(), key=operator.itemgetter(1))[0]]

            i +=1
        print(wordArray)
        print(frequencyArray)

        # display a histogram for counts
        show_histogram(frequencyArray, wordArray)

    except IOError:
        tkinter.messagebox.showwarning("Analyze File", "File " + filename + " does not exist")


def open_file():
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)


def show_histogram(frequencyArray, wordArray):
    numberOfBars = len(frequencyArray)
    width = int(canvas["width"])
    height = int(canvas["height"])
    heightBar = 0.75 * height
    widthBar = width - 20
    maxCounts = max(frequencyArray)

    for i in range(numberOfBars):
        canvas.create_rectangle(i * widthBar / numberOfBars + 10, height - 20 - frequencyArray[i] * heightBar / maxCounts,
                                (i + 1) * widthBar / numberOfBars + 10, height - 20)
        canvas.create_text(i * widthBar / numberOfBars + 10 + 0.5 * widthBar / numberOfBars, height - 10,
                           text=str(wordArray[i]))


window = Tk()
window.title("Words Frequency Histogram")

frame1 = Frame(window)
frame1.pack()
canvas = Canvas(frame1, width=500, height=200)
canvas.pack()

frame2 = Frame(window)
frame2.pack()

Label(frame2, text="Enter a filename: ").pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=40, textvariable=filename).pack(side=LEFT)
Button(frame2, text="Browse", command=open_file).pack(side=LEFT)
Button(frame2, text="Show Result", command=show_result).pack(side=LEFT)

window.mainloop()
