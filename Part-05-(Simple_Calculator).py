from tkinter import *

root = Tk()

# .title(), like the window name in the close button row
root.title('I am the title')

e = Entry(root, width=55)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#e.pack() use grids to simply design
#e.insert(0, 'Enter the values') i don't like to use

# process

# buttons

# design

root.mainloop()