from tkinter import *
from math import *
root=Tk()
root.title("FUNCTIONS")

def button(x):
    global a, ax
    ax=[
        " + ",
        " - ",
        " * ",
        " / ",

        " sin(x) ",
        " cos(x) ",
        " tan(x) ",
        " log10(x) ",
        " ln(x) ",
        " x ",

        "1","2","3","4","5","6","7","8","9","0",".",
        " ( ", " ) "

    ]
    a = str(e1.get())
    e1.delete(0, END)
    e1.insert(0, a + ax[x])

def equal(av,aft):
    e3.delete(0,END)
 #   global ab, ans, j
    rnd=3
    #ab= e1.get().split()
    ab=av
    print("ab=",end=" ")
    print(ab)
    i=0
    av=[None]*len(ab)
    ab2 = [None]*len(ab)
    print(ab2)
    k = 0
    a=0
    for bx in ab:
        if bx == '(':
            ka=0
            while i < len(ab):
                av[ka] = ab[i]
                ka = ka + 1
                if ab[i] == ')':
                    break
                i = i + 1
                k = k + 1

            h=0
            for elem in av:
                if elem == ")":
                    break
                h= h +1
            av=av[1:h]
            aft = aft +1
            ab2[i-k] = equal(av,k)
            aft = aft -1
            a = k
            av = [None] * len(ab)
        if a != 0:
            a = a - 1
            continue
        if bx == 'sin(x)':
            ab2[i-k] = sin(float(e2.get()))
        if bx == 'cos(x)':
            ab2[i-k] = cos(float(e2.get()))

        if bx == 'tan(x)':
            ab2[i-k] = tan(int(e2.get()))
        if bx == 'log10(x)':
            ab2[i-k] = log10(int(e2.get()))
        if bx == 'ln(x)':
            ab2[i-k] = log(int(e2.get()))
        if bx == 'x':
            ab2[i-k] = int(e2.get())
        if bx == '+':
            ab2[i-k]=1
        if bx == '-':
            ab2[i-k]=2
        if bx == '*':
            ab2[i-k]=3
        if bx == '/':
            ab2[i-k]=4
        if bx.replace('.','',1).isdigit():
            ab2[i-k]= float(bx)

        i = 1 + i
        print("ab2=", end=" ")
        print(ab2)

    h2 = 0
    for elem in ab2:
        if elem == None:
            break
        h2 = h2 + 1
    ab2 = ab2[0:h2]
    af=[0.0]*len(ab2)
    i=1
    k=1
    ka=False
    while i < len(ab2):
        aw = False
        if ab2[i] < 3:
            if ka == True:
                af[k]=ab2[i]
                k=k+2
                ka=False
            else:
                af[k-1]=ab2[i-1]
                af[k]=ab2[i]
                k=2 + k
        if ab2[i] == 3:
            af[k-1]=ab2[i-1]*ab2[i+1]
            ka=True
            aw = False
        if ab2[i] == 4:
            af[k-1]=ab2[i-1]/ab2[i+1]
            ka=True
            aw=True
        i=2 + i
        if i >=len(ab2) and aw == False:
            af[k-1]=ab2[len(ab2)-1]
    i = len(ab2) - 1
    print("af", end="=")
    print(af)
    while i >=0 :
        if i%2 == 1 and af[i] == 1:
            af[i-1]=af[i-1]+af[i+1]
        if i%2 == 1 and af[i] == 2:
            af[i-1]=af[i-1]-af[i+1]
        i=i-1
    if aft == 0:
        e3.insert(0,round(af[0],rnd))
    else :
        return af[0]

def clear():
    e1.delete(0,END)
def ans():
    an=e3.get()
    e1.delete(0, END)
    e1.insert(0, an )

frame=LabelFrame(root)
frame.grid(row=0,column=0,columnspan=4)

Label(frame, text="function").grid(row=0,column=0)
e1=Entry(frame)
e1.grid(row=0,column=1)
Label(frame, text="value").grid(row=1,column=0)
e2=Entry(frame)
e2.grid(row=1, column=1)
Label(frame, text="answer").grid(row=2,column=0)
e3=Entry(frame)
e3.grid(row=2, column=1)
Button(frame,text= "=",height=4,command= lambda : equal(e1.get().split(),0)).grid(row=0, column= 2,rowspan=3)






w1=5
h1=2
r0=1
but1=Button(root,text= "+",width=w1,height=h1,command=lambda : button(0))
but1.grid(row=r0, column= 0)
but2=Button(root,text= "-",width=w1,height=h1,command=lambda : button(1))
but2.grid(row=r0, column= 1)
but3=Button(root,text= "*",width=w1,height=h1,command=lambda : button(2))
but3.grid(row=r0, column= 2)
but4=Button(root,text= '/',width=w1,height=h1,command=lambda : button(3))
but4.grid(row=r0, column= 3)

r1=2
but5=Button(root,text= 'sin',width=w1,height=h1,command=lambda: button(4))
but5.grid(row=r1, column= 0)
but6=Button(root,text= 'cos',width=w1,height=h1,command=lambda: button(5))
but6.grid(row=r1, column= 1)
but7=Button(root,text= 'tan',width=w1,height=h1,command=lambda: button(6))
but7.grid(row=r1, column= 2)
but8=Button(root,text= 'log10',width=w1,height=h1,command=lambda: button(7))
but8.grid(row=r1, column= 3)

r2=3
but11=Button(root,text= "ln",width=w1,height=h1, command=lambda: button(8))
but11.grid(row=r2, column= 0,columnspan=1)
but10=Button(root,text= "x",width=w1,height=h1, command= lambda: button(9))
but10.grid(row=r2, column= 1,columnspan=1)
but10=Button(root,text= "clear",width=w1,height=h1, command= clear)
but10.grid(row=r2, column= 2,columnspan=1)
but11=Button(root,text= "(",width=w1,height=h1, command=  lambda: button(21))
but11.grid(row=r2, column= 3,columnspan=1)

r4=4
Button(root,text= "1",width=w1,height=h1,command= lambda: button(10)).grid(row=r4, column= 0)
Button(root,text= "2",width=w1, height=h1,command= lambda: button(11)).grid(row=r4, column= 1)
Button(root,text= "3",width=w1,height=h1,command= lambda: button(12)).grid(row=r4, column= 2)
Button(root,text= "4",width=w1,height=h1,command= lambda: button(13)).grid(row=r4, column= 3)

r4=5
Button(root,text= "5",width=w1,height=h1,command= lambda: button(14)).grid(row=r4, column= 0)
Button(root,text= "6",width=w1, height=h1,command= lambda: button(15)).grid(row=r4, column= 1)
Button(root,text= "7",width=w1,height=h1,command= lambda: button(16)).grid(row=r4, column= 2)
Button(root,text= "8",width=w1,height=h1,command= lambda: button(17)).grid(row=r4, column= 3)

r4=6
Button(root,text= "9",width=w1,height=h1,command= lambda: button(18)).grid(row=r4, column= 0)
Button(root,text= "0",width=w1, height=h1,command= lambda: button(19)).grid(row=r4, column= 1)
Button(root,text= ".",width=w1, height=h1,command= lambda: button(20)).grid(row=r4, column= 2)
Button(root,text= ")",width=w1, height=h1,command= lambda: button(22)).grid(row=r4, column= 3)

r5=7
Button(root,text= "ANS",width=w1, height=h1,command= ans).grid(row=r5, column= 0)
Label(root, text = "it doesnt work for brakets within brakets").grid(row=8,column = 0, columnspan = 4)

root.mainloop()