from tkinter import *
class MyButtons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.printButton = Button(frame, text="Print", command=self.printMessage)
        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.printButton.pack(side=LEFT)
        self.quitButton.pack(side=LEFT)
    def printMessage(self):
        print("It's Working!")
root = Tk()
obj = MyButtons(root)
root.mainloop()