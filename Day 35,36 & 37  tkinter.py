# tkinter, pyQT
# tkinter is a standard library in python
# tkinter used to create GUI(Graphical User Interfaces)
# steps: 1) import tkinter 2) create an instance using 'Tk' module in tkinter 3) call mainloop- here a window of tkinter is opened wher we do remaining things
# Examples of widgets in tkinter  - labels, entry
# from tkinter import*
# x=Tk()
# x.title("tkinter python file")
# x.geometry("400x400")
# x.minsize(100,100)
# x.maxsize(500,500)
# x.resizable(False,True)
# # x.resizable(True,False)
# # x.resizable(False,False)
# # x.resizable(True,True)
# x.attributes("-alpha",1)
# x.attributes("-topmost",1)
# l1=Label(x,text="Name",bg="yellow",fg="blue",width=10,height=2, anchor=CENTER, font="arial 20 underline")
# l1.grid(row=0,column=0)
# l2=Label(x,text="Email",bg="pink",fg="green",width=50,height=5,anchor=S, font="arial 40 overstrike",pady=30)
# l2.grid(row=1,column=0)
# e1=Entry(x,fg="red")
# e1.grid(row=0,column=1)
# l2=Label(x,text="Password")
# l2.grid(row=0,column=0)
# e2=Entry(x,show="*",width=20,bd=5,justify="center")
# e2.grid(row=0,column=1)

# x.configure(bg="yellow")

# l3=Label(x)
# l3.grid(row=2,column=0)

# def display():
#     print("hai")
#     l2.configure(text="Username")
#     l3.configure(text="login")

# b1=Button(x,text="click",command=display)
# b1.grid(row=1,column=1)

# print("start")
# x.mainloop()
# # print("stop")



# widgets--label, entry, button ----
from tkinter import*
x=Tk()
x.title("tkinter exercise 1")
x.geometry("400x400")
l1=Label(x,text='Name')
l1.grid(row=0,column=0)
e1=Entry(x)
e1.grid(row=0,column=1)
l2=Label(x,text="Email")
l2.grid(row=1,column=0)
e2=Entry(x)
e2.grid(row=1,column=1)
l3=Label(x,text="Phone Number")
l3.grid(row=2,column=0)
e3=Entry(x)
e3.grid(row=2,column=1)
def display():
    y=e3.get()
    print("phone number is",y)
    e3.configure(show="*")
    l3.destroy()
b1=Button(x,text="click here",command=display)
b1.grid(row=3,column=1)

x.mainloop()


# from tkinter import*
# x=Tk()
# x.title("tkinter exercise 1")
# x.geometry("400x400")

# l1=Label(x,text="Name")
# l1.grid(row=0, column=0)
# e1=Entry(x)
# e1.grid(row=0,column=1)
# l2=Label(x,text="Email")
# l2.grid(row=1,column=0)
# e2=Entry(x)
# e2.grid(row=1,column=1)
# l3=Label(x,text="Phone Number")
# l3.grid(row=2,column=0)
# e3=Entry(x)
# e3.grid(row=2,column=1)

# l4=Label(x,text=" ")
# l4.grid(row=4,column=1)
# l5=Label(x,text=" ")
# l5.grid(row=5,column=1)
# l6=Label(x,text=" ")
# l6.grid(row=6,column=1)
# l7=Label(x,text=" ")
# l7.grid(row=7,column=1)

# def show():
#     l4.configure(text="My details")
#     l5.configure(text=" My name: "+ e1.get())
#     l6.configure(text="My email: "+ e2.get())
#     l7.configure(text="My phone number: " + e3.get())
# def display():
#     l4.destroy()
#     l5.destroy()
#     l6.destroy()
#     l7.destroy()

# b1=Button(text="submit",command=show)
# b1.grid(row=3,column=1)
# b2=Button(text="delete",command=display)
# b2.grid(row=8,column=1)



# # print("start")
# x.mainloop()


# from tkinter import*
# x=Tk()
# x.title("sum of two numbers")
# x.geometry("400x400")

# a=StringVar()
# l1=Label(x,text="first number")
# l1.grid(row=0,column=0)
# e1=Entry(x)
# e1.grid(row=0,column=1)

# l2=Label(x,text="second number")
# l2.grid(row=1,column=0)
# e2=Entry(x)
# e2.grid(row=1,column=1)

# l3=Label(x,text="result")
# l3.grid(row=2,column=0)
# e3=Entry(x,textvariable=a)
# e3.grid(row=2,column=1)

# def addition():
#     sum=int(e1.get())+int(e2.get())
#     a.set(sum)

# b1=Button(x,text="submit",command=addition)
# b1.grid(row=3,column=1)
# x.mainloop()


# from tkinter import*
# x=Tk()
# x.title("radio button")
# x.geometry("400x400")

# a=StringVar()

# # l1=Label(x,text="selected gender")
# # l1.grid(row=0,column=0)
# # e4=Entry(x,textvariable=r)
# # e4.grid(row=0,column=1)

# # k=StringVar()
# b=StringVar()

# # r1=Radiobutton(x,text="female",variable=k,value="female")
# # r1.grid(row=2,column=0)
# # r2=Radiobutton(x,text="male",variable=k,value="male")
# # r2.grid(row=3,column=0)
# # r3=Radiobutton(x,text="others",variable=k,value="others")
# # r3.grid(row=4,column=0)

# # c1=Checkbutton(x,text="english")
# # c1.grid(row=6,column=1)
# # c2=Checkbutton(x,text="hindi")
# # c2.grid(row=7,column=1)
# # c3=Checkbutton(x,text="tamil")
# # c3.grid(row=8,column=1)

# # def radio():
# #     a=k.get()
# #     r.set(k.get())

# # b1=Button(x,text="selected gender",command=radio)
# # b1.grid(row=5,column=1)

# # from tkinter.ttk import Combobox
# # from tkinter.scrolledtext import ScrolledText

# # combo=Combobox(x)
# # combo['values']=("hai","hello","welcome")
# # combo.current(0)
# combo.grid(row=9,column=1)


# s1=ScrolledText(x,width=30,height=10)
# s1.grid(row=10,column=1)



# l1 = Label(x, text="ENTER FIRST DIGIT", background="#e3bce0", font=("courier 20 bold"), width=28, height=2)
# l1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
# e1 = Entry(x, font=("courier 20 bold"), width=28)
# e1.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# # Second label and entry
# l2 = Label(x, text="ENTER SECOND DIGIT", background="#bccae3", font=("courier 20 bold"), width=28, height=2)
# l2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
# e2 = Entry(x, font=("courier 20 bold"), width=28)
# e2.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# # Result label and entry
# l3 = Label(x, text="RESULT", background="#e8d9ae", font=("courier 20 bold"), width=28, height=2)
# l3.grid(row=2, column=0, padx=10, pady=10, sticky="w")
# e3 = Entry(x, textvariable=b, font=("courier 20 bold"), width=28)
# e3.grid(row=2, column=1, padx=10, pady=10, sticky="w")

# # Button to trigger the calculation
# b1 = Button(x, text="SEE RESULT", width=28, height=2, command=show, background="#54534d", fg="#d6d5d0")
# b1.grid(row=6, column=0, columnspan=2, pady=20)

# # Start the Tkinter loop
# x.mainloop()

# from tkinter import *

# root = Tk()
# root.geometry("300x200")

# # Styled Label
# label = Label(root, text="Styled Label", font=("Arial", 14, "bold"), bg="lightblue", fg="black", relief="ridge", padx=10, pady=5)
# label.pack(pady=10)

# # Styled Button
# button = Button(root, text="Styled Button", font=("Arial", 12), bg="blue", fg="white", relief="raised", bd=3)
# button.pack(pady=10)

# root.mainloop()

from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x200")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12), foreground="white", background="blue", padding=10)
style.configure("TLabel", font=("Arial", 14), foreground="black")

# Themed Label
label = ttk.Label(root, text="Styled Label", style="TLabel")
label.pack(pady=10)

# Themed Button
button = ttk.Button(root, text="Styled Button", style="TButton")
button.pack(pady=10)

root.mainloop()

