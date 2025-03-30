from tkinter import *

root = Tk()

# .title(), like the window name in the close button row
root.title('I am the title')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=2, pady=3)
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
    if nwvalv==1 and t!='+' and t!='-' and t!='*' and t!='/':
        clearf()
    i = i+t
    nwvalv = 0
    et = e.get()  # input box value handling
    e.delete(0, END)
    e.insert(0, et+str(t))

def backspace():
    global i
    e.delete(0, END)
    if len(i)<2:
        i="" 
    else:
        i=i[:-1]
        e.insert(0, i)


def clearf():  # totally clear the input box
    global i
    e.delete(0, END)   
    i=""
    

# buttons with positions
button0 = Button(root, text='0', command=lambda: (typing('0')), padx=20, pady=10)
button0.grid(row=1, column=0)

button1 = Button(root, text='1', command=lambda: (typing('1')), padx=20, pady=10)
button1.grid(row=1, column=1)

button2 = Button(root, text='2', command=lambda: (typing('2')), padx=20, pady=10)
button2.grid(row=1, column=2)

button3 = Button(root, text='3', command=lambda: (typing('3')), padx=20, pady=10)
button3.grid(row=1, column=3)

button4 = Button(root, text='4', command=lambda: (typing('4')), padx=20, pady=10)
button4.grid(row=2, column=0)

button5 = Button(root, text='5', command=lambda: (typing('5')), padx=20, pady=10)
button5.grid(row=2, column=1)

button6 = Button(root, text='6', command=lambda: (typing('6')), padx=20, pady=10)
button6.grid(row=2, column=2)

button7 = Button(root, text='7', command=lambda: (typing('7')), padx=20, pady=10)
button7.grid(row=2, column=3)

button8 = Button(root, text='8', command=lambda: (typing('8')), padx=20, pady=10)
button8.grid(row=3, column=0)

button9 = Button(root, text='9', command=lambda: (typing('9')), padx=20, pady=10)
button9.grid(row=3, column=1)

buttonclr = Button(root, text='C', command=clearf, padx=19, pady=10)
buttonclr.grid(row=3, column=2
               )
buttondel = Button(root, text='⌫', command=backspace, padx=16, pady=10)
buttondel.grid(row=3, column=3)

buttonmlt = Button(root, text='*', command=lambda: (typing('*')), padx=21, pady=10)
buttonmlt.grid(row=4, column=0)

buttondiv = Button(root, text='/', command=lambda: (typing('/')), padx=20, pady=10)
buttondiv.grid(row=4, column=1)

buttonadd = Button(root, text='+', command=lambda: (typing('+')), padx=19, pady=10)
buttonadd.grid(row=4, column=2)

buttonmns = Button(root, text='-', command=lambda: (typing('-')), padx=21, pady=10)
buttonmns.grid(row=4, column=3)

buttondot = Button(root, text='.', command=lambda: (typing('.')), padx=22, pady=10)
buttondot.grid(row=5, column=0)

buttoneql = Button(root, text='=', command=result, padx=75, pady=10)
buttoneql.grid(row=5, column=1, columnspan=3)

root.mainloop()