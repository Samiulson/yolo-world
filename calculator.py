from tkinter import *
from math import sin, cos, tan, log10, log
root = Tk()
root.title("CALCULATOR")
#root.geometry("100x100")
frame=LabelFrame(root)
frame.grid(row=0,column=0,columnspan=4)
Label(frame, text="ENTER:",height=2).grid(row=0)
e=Entry(frame)
e.grid(row=0,column=1 )


def numb(x):
    global a
    a=str(e.get())
    e.delete(0, END)
    e.insert(0, a+x)
def button(h):
    global ab,ac,ad
    ad=0
    ac=e.get()
    ab=h
    e.delete(0,END)
    if ab == 1:
        e.insert(0,"-")
        ad=1
    if ab == 10:
        e.insert(0,"sin("+ac+")")
    if ab == 11:
        e.insert(0,"cos("+ac+")")
    if ab == 12:
        e.insert(0,"tan("+ac+")")
    if ab == 13:
        e.insert(0,"log10("+ac+")")
    if ab == 14:
        e.insert(0, "ln(" + ac + ")")
def equal():
    global num
    try:
        if ab==0:
            num= float(e.get()) + float(ac)
        if ab==1:
            num= float(e.get()) - float(ac)
        if ab == 1 and ad == 1:
            num = -float(e.get()) - float(ac)

        if ab==2:
            num= float(e.get()) * float(ac)
        if ab==3:
            num= float(e.get()) / float(ac)
        if ab == 10:
            num=sin(float(ac))
        if ab == 11:
            num=cos(float(ac))
        if ab == 12:
            num=tan(float(ac))
        if ab == 13:
            num=log10(float(ac))
        if ab == 13:
            num=log(float(ac))
        e.delete(0,END)
        e.insert(0,num)
    except:
        e.delete(0,END)
        e.insert(0,"ERROR!")

def clear():
    e.delete(0,END)


w1=5
h1=2
Button(root,text= "1",width=w1,height=h1,command= lambda: numb("1")).grid(row=1, column= 0)
Button(root,text= "2",width=w1, height=h1,command= lambda: numb("2")).grid(row=1, column= 1)
Button(root,text= "3",width=w1,height=h1,command= lambda: numb("3")).grid(row=1, column= 2)
Button(root,text= "4",width=w1,height=h1,command= lambda: numb("4")).grid(row=1, column= 3)

Button(root,text= "5",width=w1,height=h1,command= lambda: numb("5")).grid(row=2, column= 0)
Button(root,text= "6",width=w1, height=h1,command= lambda: numb("6")).grid(row=2, column= 1)
Button(root,text= "7",width=w1,height=h1,command= lambda: numb("7")).grid(row=2, column= 2)
Button(root,text= "8",width=w1,height=h1,command= lambda: numb("8")).grid(row=2, column= 3)

Button(root,text= "9",width=w1,height=h1,command= lambda: numb("9")).grid(row=3, column= 0)
Button(root,text= "0",width=w1, height=h1,command= lambda: numb("0")).grid(row=3, column= 1)
Button(root,text= "=",width=w1,height=h1,command= lambda : equal()).grid(row=3, column= 2)
Button(root,text= ".",width=w1,height=h1, command= lambda: numb(".")).grid(row=3, column= 3)



but1=Button(root,text= "+",width=w1,height=h1,command=lambda : button(0))
but1.grid(row=4, column= 0)
but2=Button(root,text= "-",width=w1,height=h1,command=lambda : button(1))
but2.grid(row=4, column= 1)
but3=Button(root,text= "x",width=w1,height=h1,command=lambda : button(2))
but3.grid(row=4, column= 2)
but4=Button(root,text= '/',width=w1,height=h1,command=lambda : button(3))
but4.grid(row=4, column= 3)

but5=Button(root,text= 'sin',width=w1,height=h1,command=lambda: button(10))
but5.grid(row=5, column= 0)
but6=Button(root,text= 'cos',width=w1,height=h1,command=lambda: button(11))
but6.grid(row=5, column= 1)
but7=Button(root,text= 'tan',width=w1,height=h1,command=lambda: button(12))
but7.grid(row=5, column= 2)
but8=Button(root,text= 'log10',width=w1,height=h1,command=lambda: button(13))
but8.grid(row=5, column= 3)

but11=Button(root,text= "ln",width=14,height=h1, command=lambda: button(14))
but11.grid(row=6, column= 0,columnspan=2)
but10=Button(root,text= "Clear",width=14,height=h1, command= clear)
but10.grid(row=6, column= 2,columnspan=2)

Label(root,text="press functions then number").grid(row=7,column=0,columnspan=4)

root.mainloop()