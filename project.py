from tkinter import *
from tkinter import ttk
import random
root = Tk()
root.title('Rock Paper Scissor Game')
root.geometry('300x200')
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Rock Paper Scissor",font=("Arial", 25),foreground=("blue")).grid(column=0, row=0)
frm2 = ttk.Frame(root, padding=10)
frm.grid()
p=StringVar()
ttk.Label(frm, textvariable=p).grid(column=0, row=3)
p.set('Player     VS     Computer')
var = StringVar()
label = Label(frm , textvariable=var, relief=SOLID,background="white",width=20, height=2).grid(column=0, row=6)
frm1 = ttk.Frame(root)
frm1.grid()
def rock():
    callit(1)
def paper():
    callit(2)
def scissor():
    callit(3)
def callit(b):
    a=random.randint(1, 3)
    if(a==1):
        if(b==1):
            p.set('ROCK     VS     ROCK')
            var.set('DRAW')
        elif(b==2):
            p.set('PAPER     VS     ROCK')
            var.set('WIN')
            #var.set('Paper Always win against ROCK')
        else:
            p.set('SCISSOR     VS     ROCK')
            var.set('LOSE')
            #var.set('Sorry Scissor lost AGAINST THE BIG GREAT ROCK. TRY AGAIN!!')
    elif(a==2):
        if(b==1):
            p.set('ROCK     VS     PAPER')
            var.set('LOSE')
            #var.set('Sorry ROCK lost AGAINST PAPER. TRY AGAIN!!')
        elif(b==2):
            p.set('PAPER     VS     PAPER')
            var.set('DRAW')
        else:
            p.set('SCISSOR     VS     PAPER')
            var.set('WIN')
            #var.set('ALL HAIL ALMIGHTY SCISSOR THAT WAS A SMART CHOICE AGAINST PAPER')
    elif(a==3):
        if(b==1):
            p.set('ROCK     VS     SCISSOR')
            var.set('WIN')
            #var.set('AND THATS HOW YOU SMASHED THE POOR SCISSOR WITH YOUR MERCYLESS ROCK')
        elif(b==2):
            p.set('PAPER     VS     SCISSOR')
            var.set('LOSE')
            #var.set('CHOPPING TIME BY THE COMPUTER SHREDDED YOUR PAPER WITH SCISSOR')
        else:
            p.set('SCISSOR     VS     SCISSOR')
            var.set('DRAW')
def reset():
    var.set('')
    p.set('Player     VS     Computer')
Button(frm1, text="Rock", command=rock).grid(column=0, row=12)
Button(frm1, text="Paper", command=paper).grid(column=1, row=12)
Button(frm1, text="Scissor", command=scissor).grid(column=2, row=12)
Button(frm1, text="Reset Game", command=reset,background='black',foreground='red',width=8,height=1).grid(column=1, row=15)

root.mainloop()
