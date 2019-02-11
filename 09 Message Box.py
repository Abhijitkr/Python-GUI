from tkinter import *
import tkinter.messagebox
root = Tk()
tkinter.messagebox.showinfo("My First Window", "I want to know you more!")
answer = tkinter.messagebox.askquestion("Question 1", "Do you like Ice Cream?")
if answer == "yes":
    print("I'll get you one.")
root.mainloop()