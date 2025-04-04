from tkinter import *
import math

root = Tk()

# .title(), like the window name in the close button row
root.title('Cal : )')

e = Entry(root, width=20, borderwidth=5, font=('Courier', 12, 'bold'))
e.grid(row=0, column=0, columnspan=4, padx=2, pady=5)
#e.pack() use grids to simply design
#e.insert(0, 'Enter the values') i don't like to use

# eval() # takes a string and evaluates it as a Python expression.
i="" # full empty value to veriable
nwvalv = 0 # used to, when we get answer and we enter number again, calculator format itself to solve next math
err = 0

# process
def result():  # show the final result
    global i, nwvalv, err
    try:
        while i[0]=='0':  # fix pre 0 error
            i=i[1:]   # floats are protected by the '.', all pre )s removed
        ans = eval(i)
        if type(ans)==float and str(ans)[-2]=='.' and str(ans)[-1]=='0':  # fix floats repeat after /
            ans = int(ans)
    except (ZeroDivisionError, SyntaxError):  # handle zero division error and syntax errors
        ans = 'Error'
        err = 1
    e.delete(0, END)
    if len(str(ans))>20:
        b = math.floor(math.log10(abs(ans)))  # Find exponent
        a = ans / (10**b)  # Normalize number to scientific notation
        e.insert(0, f'{a:.12f}×10^{b}')
    else:
        e.insert(0, str(ans))  # insert the answer to I/O box
    nwvalv = 1
    i = str(ans)  # handle if the answer require to further processes


def typing(t):  # hadles what's typing from the GUI
    global i, nwvalv, err  # undate the i globally i for last result
    if nwvalv==1 and t!='+' and t!='-' and t!='*' and t!='/' or err==1:
        clearf()
        err=0
    i = i+t
    nwvalv = 0
    et = e.get()  # input box value handling
    e.delete(0, END)
    if len(et+str(t))>20:
        e.insert(0, et[1:]+str(t))
    else:
        e.insert(0, et+str(t))

def backspace():  # handle Backspace requests
    global i
    e.delete(0, END)
    if len(i)<2:  # fix empty backspace errors
        i="" 
    else:
        i=i[:-1]
        e.insert(0, i)


def clearf():  # totally clear the input box
    global i
    e.delete(0, END)   
    i=""
    

# buttons with positions
button0 = Button(root, text='0', command=lambda: (typing('0')), padx=20, pady=10, bg='#FFDE21', font=('Helvetica', 10, 'bold'))
button0.grid(row=1, column=0)

button1 = Button(root, text='1', command=lambda: (typing('1')), padx=20, pady=10, bg='#FFDE21', font=('Helvetica', 10, 'bold'))
button1.grid(row=1, column=1)

button2 = Button(root, text='2', command=lambda: (typing('2')), padx=20, pady=10, bg='#FFDE21', font=('Helvetica', 10, 'bold'))
button2.grid(row=1, column=2)

button3 = Button(root, text='3', command=lambda: (typing('3')), padx=20, pady=10, bg='#FFDE21', font=('Helvetica', 10, 'bold'))
button3.grid(row=1, column=3)

button4 = Button(root, text='4', command=lambda: (typing('4')), padx=20, pady=10, bg='#FFDE21', font=('Helvetica', 10, 'bold'))
button4.grid(row=2, column=0)

button5 = Button(root, text='5', command=lambda: (typing('5')), padx=20, pady=10, bg='#FFDE21', font=('Helvetica', 10, 'bold'))
button5.grid(row=2, column=1)

button6 = Button(root, text='6', command=lambda: (typing('6')), padx=20, pady=10, bg='#FFDE21', font=('Helvetica', 10, 'bold'))
button6.grid(row=2, column=2)

button7 = Button(root, text='7', command=lambda: (typing('7')), padx=20, pady=10, bg='#FFDE21', font=('Helvetica', 10, 'bold'))
button7.grid(row=2, column=3)

button8 = Button(root, text='8', command=lambda: (typing('8')), padx=20, pady=10, bg='#FFDE21', font=('Helvetica', 10, 'bold'))
button8.grid(row=3, column=0)

button9 = Button(root, text='9', command=lambda: (typing('9')), padx=20, pady=10, bg='#FFDE21', font=('Helvetica', 10, 'bold'))
button9.grid(row=3, column=1)

buttonclr = Button(root, text='AC', command=clearf, padx=16, pady=11.4, bg='#BF2626', font=('Helvetica', 9, 'bold'))
buttonclr.grid(row=3, column=2
               )
buttondel = Button(root, text='⌫', command=backspace, padx=16, pady=11, bg='#C45924', font=('Helvetica', 9, 'bold'))
buttondel.grid(row=3, column=3)

buttonmlt = Button(root, text='*', command=lambda: (typing('*')), padx=17,pady=3, bg='#0060BF', font=('Helvetica', 15, 'bold'))
buttonmlt.grid(row=4, column=0)

buttondiv = Button(root, text='/', command=lambda: (typing('/')), padx=17.5, pady=3, bg='#0060BF', font=('Helvetica', 15, 'bold'))
buttondiv.grid(row=4, column=1)

buttonadd = Button(root, text='+', command=lambda: (typing('+')), padx=14.5, pady=3, bg='#0060BF', font=('Helvetica', 15, 'bold'))
buttonadd.grid(row=4, column=2)

buttonmns = Button(root, text='-', command=lambda: (typing('-')), padx=17, pady=3, bg='#0060BF', font=('Helvetica', 15, 'bold'))
buttonmns.grid(row=4, column=3)

buttondot = Button(root, text='.', command=lambda: (typing('.')), padx=18, pady=5, bg='#FFDE21', font=('Helvetica', 14, 'bold'))
buttondot.grid(row=5, column=0)

buttoneql = Button(root, text='=', command=result, padx=73, pady=5, bg='#1DA80E', font=('Helvetica', 14, 'bold'))
buttoneql.grid(row=5, column=1, columnspan=3)

root.mainloop()


# Buttons - Extra Simple way to code the button positions 
'''
buttons = [('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('AC', 5, 0), ('⌫', 5, 1)]

for (text, row, col) in buttons:
	if text == "=":
		btn = tk.Button(self.root, text=text, width=5, height=2,command=self.calculate)
	elif text == "C":
		btn = tk.Button(self.root, text=text, width=5, height=2, command=self.clear_last)
	elif text == "AC":
		btn = tk.Button(self.root, text=text, width=5, height=2, command=self.clear_all)
	elif text == "⌫":
		btn = tk.Button(self.root, text=text, width=5, height=2, command=self.backspace)
	else:
		btn = tk.Button(self.root, text=text, width=5, height=2, command=lambda t=text: self.add_to_entry(t))
	btn.grid(row=row, column=col, padx=5, pady=5)
'''