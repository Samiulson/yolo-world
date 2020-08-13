from tkinter import *
from math import *
root=Tk()
root.title("FUNCTIONS")
timer = 0
def button(x,fnumb):
    global a, ax, timer,nj,anm
    ax=[
        " + ",
        " - ",
        " * ",
        " / ",

        "sin(x)",
        "cos(x)",
        "tan(x)",
        "log10(x)",
        "ln(x)",
        "x",

        "1","2","3","4","5","6","7","8","9","0",".",
        " ( ", " ) ",
        " []^[] ",
        "e"

    ]

    if fnumb == 2:
        timer = fnumb
        a = str(e1.get())
        e1.delete(0, END)
        e1.insert(0, a + ax[x])
        anm = True
    if x != 23:
        if timer != 0:
            e1.delete(0, END)
            if timer == 1:
                e1.insert(0, a + nj[0:6] + ax[x] + nj[6:8])
                timer = timer - 1

            if timer == 2:
                nj = ax[23][0:2] + ax[x] + ax[23][2:7]
                e1.insert(0, a + nj)
                timer = timer - 1
        else:
            a = str(e1.get())
            e1.delete(0, END)
            e1.insert(0, a + ax[x])
def equal(ab,aft):
    print("recursion number=" + str(aft))
    e3.delete(0,END)
    rnd=3
    print("ab=",end=" ")
    print(ab)
    i=0
    av=[None]*len(ab)
    ab2 = [None]*len(ab)
    k = 0
    a=0
    h2 = 0
    for elem in ab:
        if elem == None:
            break
        h2 = h2 + 1
    ab = ab[0:h2]
    j=0
    while j < len(ab):
        if a != 0:
            a = a - 1
            j = j + 1
            continue

        if ab[j] == '(':

            aft = aft + 1
            hk=0
            ka=0
            while i < len(ab):
                av[ka] = ab[i]
                ka = ka + 1
                if ab[i] == '(':
                    hk = hk + 1
                if ab[i] == ')':
                    hk = hk - 1

                if ab[i] == ')' and hk == 0:
                    break
                i = i + 1
                k = k + 1
            av=av[1:k]
            ab2[i-k] = equal(av,aft)
            print("here ab2=", end="")
            print(ab2)
            aft = aft -1
            if aft == 0:
                ab = ab2
            h2 = 0
            for elem in ab:
                if elem == None:
                    break
                h2 = h2 + 1
            ab = ab[0:h2]
            a = k
            av = [None] * len(ab)
        if a != 0:
            a = a - 1
            j = j + 1
            continue
        if ab[j] == 'sin(x)':
            ab2[i-k] = sin(float(e2.get()))
        if ab[j] == 'cos(x)':
            ab2[i-k] = cos(float(e2.get()))

        if ab[j] == 'tan(x)':
            ab2[i-k] = tan(int(e2.get()))
        if ab[j] == 'log10(x)':
            ab2[i-k] = log10(int(e2.get()))
        if ab[j] == 'ln(x)':
            ab2[i-k] = log(int(e2.get()))
        if ab[j] == 'x':
            ab2[i-k] = int(e2.get())
        if ab[j] == '+':
            ab2[i-k]=1
        if ab[j] == '-':
            ab2[i-k]=2
        if ab[j] == '*':
            ab2[i-k]=3
        if ab[j] == '/':
            ab2[i-k]=4
        if ab[j].replace('.','',1).isdigit():
            ab2[i-k]= float(ab[j])
        if ab[j][0] == '[':
            if ab[j][1].replace('.','',1).isdigit() and ab[j][5].replace('.','',1).isdigit():
                ab2[i-k]=pow(float(ab[j][1]),float(ab[j][5]))
            if ab[j][1].replace('.', '', 1).isdigit() and ab[j][5] == "x":
                ab2[i-k] = pow(float(ab[j][1]),float(e2.get()))
            if ab[j][5].replace('.', '', 1).isdigit() and ab[j][1] == "x":
                ab2[i-k] = pow(float(e2.get()),float(ab[j][5]))
            if ab[j][1] == "e" and ab[j][5].replace('.', '', 1).isdigit():
                ab2[i-k] = exp(float(ab[j][5]))
            if ab[j][1] == "e" and ab[j][5] == "x":
                ab2[i-k] = exp(float(e2.get()))
            if ab[j][1] == "x" and ab[j][5] == "e":
                ab2[i-k] = pow(float(e2.get()),exp(1))


        if ab[j] == "e":
            ab2[i-k] = exp(1)
        i = 1 + i
        j = j + 1
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
    if len(ab2) == 1:
        if aft == 0:
            e3.insert(0,round(ab2[0],rnd))
        else :
            return ab2[0]
    else:
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
        i = len(af) - 1
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
            print("af[0]="+str(af[0]))
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
but1=Button(root,text= "+",width=w1,height=h1,command=lambda : button(0,0))
but1.grid(row=r0, column= 0)
but2=Button(root,text= "-",width=w1,height=h1,command=lambda : button(1,0))
but2.grid(row=r0, column= 1)
but3=Button(root,text= "*",width=w1,height=h1,command=lambda : button(2,0))
but3.grid(row=r0, column= 2)
but4=Button(root,text= '/',width=w1,height=h1,command=lambda : button(3,0))
but4.grid(row=r0, column= 3)

r1=2
but5=Button(root,text= 'sin',width=w1,height=h1,command=lambda: button(4,0))
but5.grid(row=r1, column= 0)
but6=Button(root,text= 'cos',width=w1,height=h1,command=lambda: button(5,0))
but6.grid(row=r1, column= 1)
but7=Button(root,text= 'tan',width=w1,height=h1,command=lambda: button(6,0))
but7.grid(row=r1, column= 2)
but8=Button(root,text= 'log10',width=w1,height=h1,command=lambda: button(7,0))
but8.grid(row=r1, column= 3)

r2=3
but11=Button(root,text= "ln",width=w1,height=h1, command=lambda: button(8,0))
but11.grid(row=r2, column= 0,columnspan=1)
but10=Button(root,text= "x",width=w1,height=h1, command= lambda: button(9,0))
but10.grid(row=r2, column= 1,columnspan=1)
Button(root,text= "[]^[]",width=w1, height=h1,command = lambda: button(23,2)).grid(row=r2, column= 2)
Button(root,text= "e",width=w1, height=h1,command = lambda: button(24,0)).grid(row=r2, column= 3)

r3=4
Button(root,text= "ANS",width=w1, height=h1,command= ans).grid(row=r3, column= 0)
but10=Button(root,text= "clear",width=w1,height=h1, command= clear)
but10.grid(row=r3, column= 1,columnspan=1)
but11=Button(root,text= "(",width=w1,height=h1, command=  lambda: button(21,0))
but11.grid(row=r3, column= 3,columnspan=1)
r4=5
Button(root,text= "1",width=w1,height=h1,command= lambda: button(10,0)).grid(row=r4, column= 0)
Button(root,text= "2",width=w1, height=h1,command= lambda: button(11,0)).grid(row=r4, column= 1)
Button(root,text= "3",width=w1,height=h1,command= lambda: button(12,0)).grid(row=r4, column= 2)
Button(root,text= "4",width=w1,height=h1,command= lambda: button(13,0)).grid(row=r4, column= 3)

r5=6
Button(root,text= "5",width=w1,height=h1,command= lambda: button(14,0)).grid(row=r5, column= 0)
Button(root,text= "6",width=w1, height=h1,command= lambda: button(15,0)).grid(row=r5, column= 1)
Button(root,text= "7",width=w1,height=h1,command= lambda: button(16,0)).grid(row=r5, column= 2)
Button(root,text= "8",width=w1,height=h1,command= lambda: button(17,0)).grid(row=r5, column= 3)

r6=7
Button(root,text= "9",width=w1,height=h1,command= lambda: button(18,0)).grid(row=r6, column= 0)
Button(root,text= "0",width=w1, height=h1,command= lambda: button(19,0)).grid(row=r6, column= 1)
Button(root,text= ".",width=w1, height=h1,command= lambda: button(20,0)).grid(row=r6, column= 2)
Button(root,text= ")",width=w1, height=h1,command= lambda: button(22,0)).grid(row=r6, column= 3)

#Label(root, text = "it doesnt work for brakets within brakets").grid(row=8,column = 0, columnspan = 4)

root.mainloop()
