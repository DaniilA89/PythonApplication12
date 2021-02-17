from tkinter import *

def lahenda():
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
        elif D==0:
            x1_round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
        else:
            t="Корней нет"
        vastus.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        elif b.get()=="":
            b.configure(bg="red")
        elif c.get()=="":
            c.configure(bg="red")

def klikker():
    pass
    

aken=Tk()
aken.title("Tkinter_app")
aken.geometry("600x300")#razmer okna
aken.iconbitmap("akeen.ico")



vastus=Label(aken,text="Решение квадратных уравнений",bg="blue",fg="yellow",font="Arial 20",height=1,width=30,borderwidth=5,relief="groove")
vastus.pack(side=TOP)

vastus=Label(aken,text="Решение",bg="yellow",fg="blue",font="Arial 20",height=3,width=10,borderwidth=5,relief="groove")
vastus.pack(side=BOTTOM)

a=Entry(aken,width=3,borderwidth=10,font="Arial 20")
a.pack(side=LEFT)

x2=Label(aken,text="x**2+",font="Arial 20",height=1,width=4,borderwidth=5,relief="groove")
x2.pack(side=LEFT)

b=Entry(aken,width=3,borderwidth=10,font="Arial 20")
b.pack(side=LEFT)

x=Label(aken,text="x+",font="Arial 20",height=1,width=4,borderwidth=5,relief="groove")
x.pack(side=LEFT)
         
c=Entry(aken,width=3,borderwidth=10,font="Arial 20")
c.pack(side=LEFT)

y=Label(aken,text="=0",font="Arial 20",height=1,width=4,borderwidth=5,relief="groove")
y.pack(side=LEFT)

btn=Button(aken,text="Решить",bg="pink",fg="green",font="Arial 20",height=1,width=30,command=lambda:lahenda())#lkm-klikker()
btn.pack(side=LEFT)



aken.mainloop()
