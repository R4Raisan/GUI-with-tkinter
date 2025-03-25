from tkinter import *

root = Tk() # starting

# Just create the Input Box  |  # can't use  hight
e = Entry(root, borderwidth=10, width=50, bg='green', fg='black')
e.pack()

e.get() # input for using 

def click():
    label1 = Label(root, text='Hi '+e.get()+'...!') # e.get()
    label1.pack()

button1 = Button(root, text='Submit', command=click)
button1.pack()

root.mainloop() # ending