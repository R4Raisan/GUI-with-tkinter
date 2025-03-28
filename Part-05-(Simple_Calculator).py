from tkinter import *

root = Tk()

# .title(), like the window name in the close button row
root.title('I am the title')

e = Entry(root, width=30)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#e.pack() use grids to simply design
#e.insert(0, 'Enter the values') i don't like to use

# eval() # takes a string and evaluates it as a Python expression.
i="" # full empty value to veriable
nwvalv = 0 # used to, when we get answer and we enter number again, calculator format itself to solve next math

# process
def result():  # show the final result
    global i, nwvalv
    ans = eval(i)
    e.delete(0, END)
    e.insert(0, str(ans))
    nwvalv = 1
    i = str(ans)

def typing(t):
    global i, nwvalv  # undate the i globally i for last result
    if nwvalv==1 and t!='+' and t!='-':
        clearf()
    i = i+t
    nwvalv = 0
    et = e.get()  # input box value handling
    e.delete(0, END)
    e.insert(0, et+str(t))

def clearf():  # totally clear the input box
    e.delete(0, END)
    global i 
    i=""
    

# buttons with positions
button0 = Button(root, text='0', command=lambda: (typing('0')), padx=20, pady=10)
button0.grid(row=2, column=0)

button1 = Button(root, text='1', command=lambda: (typing('1')), padx=20, pady=10)
button1.grid(row=2, column=1)

button2 = Button(root, text='2', command=lambda: (typing('2')), padx=20, pady=10)
button2.grid(row=2, column=2)

button3 = Button(root, text='3', command=lambda: (typing('3')), padx=20, pady=10)
button3.grid(row=3, column=0)

button4 = Button(root, text='4', command=lambda: (typing('4')), padx=20, pady=10)
button4.grid(row=3, column=1)

button5 = Button(root, text='5', command=lambda: (typing('5')), padx=20, pady=10)
button5.grid(row=3, column=2)

button6 = Button(root, text='6', command=lambda: (typing('6')), padx=20, pady=10)
button6.grid(row=4, column=0)

button7 = Button(root, text='7', command=lambda: (typing('7')), padx=20, pady=10)
button7.grid(row=4, column=1)

button8 = Button(root, text='8', command=lambda: (typing('8')), padx=20, pady=10)
button8.grid(row=4, column=2)

button9 = Button(root, text='9', command=lambda: (typing('9')), padx=20, pady=10)
button9.grid(row=5, column=0)

buttonadd = Button(root, text='+', command=lambda: (typing('+')), padx=20, pady=10)
buttonadd.grid(row=5, column=1)

buttonmns = Button(root, text='-', command=lambda: (typing('-')), padx=20, pady=10)
buttonmns.grid(row=5, column=2)

buttonclr = Button(root, text='C', command=clearf, padx=20, pady=10)
buttonclr.grid(row=6, column=0)

buttonans = Button(root, text='=', command=result, padx=58, pady=10)
buttonans.grid(row=6, column=1, columnspan=2)

root.mainloop()