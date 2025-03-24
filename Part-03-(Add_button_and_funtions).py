from tkinter import *

root = Tk() # starting

# normal function calling with (), with command no () using
def click():
    labelb = Label(root, text='Clicked..!')
    labelb.pack()

# Make label
label1 = Label(root, text='Hellow World!')
label2 = Label(root, text='My name is Rashen')

button1 = Button(root, text='Click Here', command=click, padx=5, pady=2, fg='blue', bg='yellow')
# command = function name without ()
button1.pack()

root.mainloop() # ending
