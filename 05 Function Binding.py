# METHOD NO.1

# from tkinter import *
# root = Tk()
# def printName():
#     print("My Name is Abhijit")
# button = Button(root, text="Print My Name",command=printName)
# button.pack()    
# root = mainloop()

# METHOD NO.2

from tkinter import *
root = Tk()
def printName(event):
    print("My Name is Abhijit.")
button = Button(root, text="What is Your Name?")
button.bind("<Button-1>", printName)
button.pack()
root.mainloop()