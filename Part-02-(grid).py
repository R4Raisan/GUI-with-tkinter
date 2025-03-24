from tkinter import *

root = Tk()

# Make labels
label1 = Label(root, text='Hellow World!')
label2 = Label(root, text='My name is Rashen')

# stay stable, spacing as using
label1.grid(row=0, column=0) # also like label1 = Label(root, text='Hellow World!').grid(row=0, column=0)
label2.grid(row=5, column=7) 
# no matter which is the grid value, because empty grids are don't display in the output

root.mainloop()