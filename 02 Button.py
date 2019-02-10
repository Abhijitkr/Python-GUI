# from tkinter import *
# root = Tk()
# button1 = Button(text="Click Me!", bg="gray", fg="blue").pack()
# root.mainloop()

from tkinter import *
root = Tk()
topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
label = Label(bottomFrame, text="Abhijit", fg="red")
label.pack()
button = Button(topFrame, text="TOP", bg="green")
button.pack()
root.mainloop()