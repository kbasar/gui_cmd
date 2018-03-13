from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
var = StringVar()

def callback():
    var.set(e.get())

e.focus_set()
b = Button(root, text="submit", width=10, command=callback)
b.pack()
label = Label( root, textvariable=var, relief=RAISED)
label.pack()
root.mainloop()