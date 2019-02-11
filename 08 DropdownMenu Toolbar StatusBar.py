from tkinter import *
def doNothing():
    print("I won't do anything!")
root = Tk()
# **** Main Menu ****
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project..", command=doNothing)
subMenu.add_command(label="New..", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.quit)
editMenu = Menu(menu) 
menu.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="Run", command=doNothing)
# **** Toolbar ****
toolbar = Frame(root, bg="gray")
insertTool = Button(toolbar, text="Insert", command=doNothing)
printTool = Button(toolbar,text="Print", command=doNothing)
insertTool.pack(side=LEFT, padx=2, pady=2)
printTool.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(fill=X)
# **** Status Bar ****
statusBar = Label(root, text="Loading Nothing...", bd=1, relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)
root.mainloop()