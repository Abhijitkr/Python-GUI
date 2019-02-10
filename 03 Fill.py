from tkinter import *
root = Tk()
label1 = Label(root, text="one", bg="red", fg="white")
label2 = Label(root, text="two", bg="blue", fg="white")
label3 = Label(root, text="three", bg="green", fg="white")
label1.pack()
label2.pack(side=LEFT, fill=Y)
label3.pack(fill=X)
root.mainloop()