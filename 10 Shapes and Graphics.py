from tkinter import *
import tkinter.messagebox
def deleteGreenRectangle():
    canvas.delete(greenRectangle)
def deleteAll():
    canvas.delete(ALL)
root = Tk()
canvas = Canvas(root, width=300, height=200)
blackLine = canvas.create_line(0, 0, 280, 100)
redLine = canvas.create_line(0, 200, 280, 100, fill="red")
greenRectangle = canvas.create_rectangle(25, 25, 250, 100, fill="green")
toolbar = Frame(root)
deleteLabel = Label(toolbar, text="Delete:---")
deleteLabel.pack()
toolbar.pack(side=TOP, fill=X)
deleteGreenRectangle = Button(toolbar, text="Green Rectangle", command=deleteGreenRectangle)
deleteGreenRectangle.pack(anchor=N, padx=2)
deleteAll = Button(toolbar, text="All", command=deleteAll)
deleteAll.pack(anchor=N)
canvas.pack()
root.mainloop()