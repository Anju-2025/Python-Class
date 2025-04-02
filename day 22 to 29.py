# # LOCAL AND GLOBAL VARIABLE
# # # x is a global variable hence, accessible both inside and outside a function
# x=10 
# def show():
#     print(x)
   

# show()

# print(x)


# # # here x is a local variable , hence accessible only inside a function, since its declared inside a function
# def show():
#     x=20
#     print(x)

# show()
# print(x)


# # x is a global variable hence accesible both inside and outside the function, even if declared inside the function
# def show():
#     global x
#     x=50
#     print(x)
# show()
# print(x)





# inbuilt modules in python  or libraries

# import math
# print(math.factorial(5))
# print(math.pow(5,3))
# print(math.lcm(2,3,4,5))
# print(math.ceil(1.2))
# print(math.floor(1.2))

# from math import factorial
# print(factorial(5))

# from math import *
# print(factorial(5))
# print(pow(3,2))
# print(lcm(2,3,4,5))
# print(ceil(1.2))
# print(floor(1.2))

import random

# x=[10,1,2,3,4,5,6]
# random.shuffle(x)
# print(x)
# print(random.choices(x))
# print(random.sample(x,5))


# print(random.randint(1,8))
# print(random.randrange(2,9,1))




# strf--string format time
# import datetime
# x=datetime.datetime.now()
# # print(x)
# print(x.strftime("%B"))                   
# print(x.strftime("%b"))
# print(x.strftime("%Y"))
# print(x.strftime("%y"))
# print(x.strftime("%A"))
# print(x.strftime("%a"))
# print(x.strftime("%m"))
# print(x.strftime("%d"))

# # # # strftime- string format time - to convert date and time to human readable format


# # def factorial(n):
# #     fact=1
# #     for i in range(1,n+1):
# #         fact*=i
# #     print(fact)

# # factorial(5)


# oops--object oriented programming--object

# def show():
#     pass
# show()


# d=10
# h='hello'

# # class, object,attributes, methods--oops
# # 

# class NewClass:
#     s=10
#     f='hello'
#     k=[10,20,50]

#     def new(self, a, b):
#         self.a=a
#         self.b=b
#         print('hello', a+b)

#     def show(self):
#         self.k=self.a*self.b
#         print('hai', self.k)

# n1=NewClass()
# n2=NewClass()
# print(n1.f)
# n1.count=200
# print(n1.count)
# n1.new(10,20)
# n1.show()

# self===current instance/current object reference
# self.a----instance variable












# # # write a dummy program that can perform login and registration using a menu driven program

# # database={}
# # def register():
# #     username=input("Enter username: ")
# #     password=input("Enter password: ")
# #     if username in database:
# #         print("username already exist, pls try again")
# #     else:
# #         database[username]=password
# #         print("Registration successful")
# # def login():
# #     username=input("Enter username: ")
# #     password=input("Enter password: ")
# #     if username in database and database[username]==password:
# #         print("Login successful")
# #     else:
# #         print("Invalid username or password")
# # def main():
# #     while True:
# #         print("\nMenu: ")
# #         print("1.Register")
# #         print("2.Login")
# #         print("3.Exit")
# #         choice=input("Enter your choice: ")
# #         if choice=='1':
# #             register()
# #         elif choice =='2':
# #             login()
# #         elif choice=='3':
# #             print("Exiting")
# #             break
# #         else:
# #             print("Invalid choice, please select a valid option")
# # main()


# # #generate 100 random lottery tickets and pick two lucky ticktes from it as winners
# import random 
# lottery_ticketslist=[]
# for i in range(100):
#     lottery_ticketslist.append(random.randint(1000,5001))
# win=random.sample(lottery_ticketslist,3)
# print("winners are",win)

# # #generate three random integers between 100 and 999 and which are divisible by 5

# import random
# k=[]
# for i in range(100,1000):
#     if i%5==0:
#         k.append(i)
# w=random.sample(k,3)
# print(w)


# # # write a program to play a game randomly choosing three numbers.

# import random
# win=5
# attempt=1
# while attempt<=3:
#     number=random.randint(0,5)
#     print(number)
#     if number==win:
#         print("You won")
#         break
#     else:
#         attempt+=1
#         print("You lost")
# else:
#     print("Game Over")

# # # # def show(n):
# # # #     fact=1
# # # #     for i in range(1,n+1):
# # # #         fact*=i
# # # #     return fact
    
# # # # print(show(6))

# # # def show():
# # #     pass
# # # show()

# #                                                         # OOPS - object oriented program 

# # class, object, methods, attributes, object is a house and class is its plan.
# # attributes- features. methods - functions

# # Example: class CAR
# # object - BMW, Benz, Audi
# # Attributes- colour,speed
# # Methods- Driving, Skid  (Funtcions it can do)


# self---current instance/current object
# b======instance variable ----all functions access
# class NewClass:
#     count=20
#     standard="V"

#     def show(self, b):
#         self.b=b
#         print("hello", b)

#     def new(self):
#         print("new function", self.b)

# c1=NewClass()
# c2=NewClass()
# print(c1.count)
# print(c2.standard)
# c1.show(10)
# c1.new()
# c2.length='25 m'
# c1.width='30m'
# print(c2.length)
# print(c1.width)







# camelcase method
# class ClassName:
#     pass
# c1=ClassName()
# c2=ClassName()

# whem we create/declare an object ---function -constructor -__init__


# self --current instance

# class Human:
#     eyes=2
#     skin="brown"

#     def vision(self, a, b):
#         self.a=a
#         self.b=b
#         print("hai",a, b)

#     def show(self):
#         print(self.a, "value in show method")
#         self.c=self.a + self.b
#         print(self.c)

        

# h1=Human()
# h2=Human()
# # print(h1.skin)
# # print(h2.skin)
# # h1.tooth=32
# # print(h1.tooth)
# h1.vision(10,20)
# h1.show()













# class Human:

#     eyes=2
#     skin='brown'
#     def __init__(self,a,b):
#         print('comstructor declared', a+b)

#     def home(self, c,d):
#         self.c=c
#         self.d=d
#         print('hai', c)

#     def display(self, w):
#         self.w=w
#         self.k=self.c + self.d
#         print(self.k)

#     def __del__(self):
#         print('destructor created')

# h1=Human(10,20)
# h1.home('python','django')
# print(h1.eyes)
# h1.teeth=32
# print(h1.teeth)
# h1.display(100)
# del h1
# print(h1.teeth)

# self.c----c----instance variable

# oops--object oriented p l

# object/instance

# self--instance variable
# class Human:
#     eyes=2
#     head=1

#     def vision(self, a, b):
#         self.a=a
#         self.b=b
#         print('hello', a+b,"vision")

#     def show(self):
#         print(self.a+self.b,"is the output of show function")

    
# h1=Human()
# h2=Human()
# print(h1.eyes)
# h1.legs=2
# h1.vision(10,20)
# h1.show()
# print(h1.legs)
# print(h2.legs)


# # vision ---object/instance --h2, self --reference of current object


# oops--object oriented programming --class, object, attribute, method

# class ClassName:
#     count=20
#     length='3m'

#     def new_function(self,a):
#         self.a=a
#         print(a)

#     def show(self):
#         print("hai", self.a)

# c1=ClassName()
# c2=ClassName()
# print(c1.length)
# print(c2.count)
# c1.width='5m'
# print(c1.width)


# c1.new_function(1000)
# c1.show()

# # self.a----instance variable --a



# class Human:
#     pass

# h1=Human()











# # class Man:
# #     # attribute
# #     eyes=2
# #     leg=2
# #     mouth=1
# #     # methods/ functions
# #     def run(self):
# #         print("running man")
# #     def walk():
# #         pass
    

# # m1=Man()
# # m2=Man()
# # print(m1.eyes)
# # print(m1.leg)
# # print(m2.mouth)
# # m2.tooth=32
# # m1.skin="brown"
# # print(m2.tooth)
# # print(m1.skin)
# # m1.run()

# # self ---instance / object variable



# # Human---class
# # eyes ---attribute
# # vision --method/function
# # h1--object/instance
# # self --current instance
# # self.a---instance variable----can pass variable to multiple functions
# # class Human:
# #     eyes=2
# #     head=1

# #     def vision(self):
# #         print("human have vision features")

# #     def show(self, a, b):
# #         self.a=a
# #         self.b=b
# #         print("demo function")
# #         print(a+b)
# #     def display(self):
# #         print(self.a+self.b)

# # h1=Human()
# # h2=Human()
# # print(h1.eyes)
# # h1.vision()
# # h1.teeth=32
# # print(h1.teeth)
# # h1.show(10,20)
# # h1.display()

# # inheritance, abstarction, polymorphism, encapsulation














# # def show(n):
# #     print(n)
# # show(20)
# # class Classname:
# #     pass
# # obj=Classname()
# # obj2=Classname()
# # a1=Classname()

# # self----instance variable (object/instance)

# # class ClassA:
# #     pass
# #     # attributes
# #     count=50
# #     paint="red"
# #     # methods
# #     def AC_Room(self):
# #         print("room is air conditioned")
# #     def show(self,a):
# #         print(a)

# # obj1=ClassA()
# # print(obj1.count)
# # print(obj1.paint)
# # obj1.AC_Room()
# # obj1.show("hello")
# # obj1.length=20
# # print(obj1.length)


# # class ClassB:
# #     def funct1(self, a,b):
# #         self.a=a
# #         self.b=b
# #     def show(self):
# #         print(self.a)
# #     def sum(self):
# #         self.c=self.a + self.b
# #         self.d=self.a - self.b
# #         print(self.c)
# #         print(self.d)
    


# # b1=ClassB()
# # b1.funct1(10, 20)
# # b1.show()
# # b1.sum()


# while we create an object -- constructor

# class Human:
#     skin='brown'
#     eyes=2

#     def __init__(self,a,b):
#         print("constructor created",a+b)

#     def vision(self,c,d):
#         self.c=c
#         self.d=d
#         print('hello',c)

#     def show(self):
#         print('hai',self.c)
#         self.k=self.c + self.d
#         print(self.k)

#     def __del__(self):
#         print('destructor created')




# h1=Human(10,20)
# h1.vision('python','django')
# h1.show()

# del h1

# print(h1.eyes)



# encapsulate
# access modifiers -- public, private, protected


# class Human:
#     def show():
#         print("hai")
# h1=Human()
# h1.show()


# class Human:
#     def __show(self):
#         print("hai")
#     def display(self):
#         self._show()
# h1=Human()
# h1.__show()
# h1.display()



# class Human:
#     def _show(self):
#         print("hai")
#     def display(self):
#         self._show()

# class Male(Human):
#     def power(request):
#         print('man power')


# h1=Human()

# m1=Male()
# h1._show()
# h1.display()
# m1.power()
# m1._show()

# public ---access outside class --all object
# private--inside class --public function -- instance

# protected --same class objects, subclass objects













# # # syntax of class
# # class Classname:
# #     pass
# # obj=Classname()
# # a1=Classname()


# # class Classname:
# #     pass
# # a1=Classname()

# # type of arguments:

# # arbitrary arguments(*args)

# def show(*k):
#     print(k)

# show(10, 20, 30, True, "Hello")

# # # keyword argument(kwargs)

# def show(b, c, a):
#     print(a)
#     print(c)
#     print(b)
# show(a=10,b=20,c=30)


# # arbitrary keyword argument(**kwargs)

# def show(**k):
#     print(k)

# show(a=10,b=20,c=30)
# # # self-----instance variable/ object bariable

# # class Classname:
# #     v=20
# #     b=30

# #     def display(self):
# #         print("hello")

# # a1=Classname()
# # print(a1.v)
# # a1.display()

# # /instance variable
# # class Classname:
# #     v=20
# #     b=30

# #     def display(self, s1, s2):
# #         self.s1=s1
# #         self.s2=s2
# #         print("hello", self.s1, self.s2)

# #     def show(self):
# #         self.c=self.s1 + self.s2
# #         print(self.c)

# #     def home(self):
# #         print(self.c, self.s1 , self.s2)

# # a1=Classname()
# # print(a1.v)
# # a1.display(20, 30)
# # a1.show()
# # a1.home()


# # add student, remove student, rejoin student, show all students


# # method overriding
# class Human:
#     def play(self):
#         print("playing")
# class Man(Human):
#     def play(self):
#         super().play()
#         print('PLAYING')
# m=Man()
# m.play()

# method overriding and constructor over riding
# class Human:
#     def __init__(self):
#         print('parent constructor')
#     def play(self):
#         print("playing")
# class Man(Human):
#     def __init__(self):
#         super().__init__()
        
#         print("child constructor")
#     def play(self):
#         super().play()
       
#         print('PLAYING')
# m=Man()
# m.play()




# # Example:
# # class Human:
# #     eyes=2
# #     ears=2
# #     mouth=1
# # h1=Human()
# # h2=Human()
# # print(h2.mouth)
# # print(h1.eyes)
# # h1.tooth=32
# # h2.skin="brown"
# # print(h1.tooth)
# # print(h2.skin)
# # inheritance, encapsulation, abstraction, polymorphism


# # self---instance variable/object variable
# # class Human:

# #     def walk(self, a, b):
# #         self.a=a
# #         self.b=b
# #         print(self.a, self.b)

# #     def show(self):
# #         print(self.a +'**'+ self.b)


# #     def display(self, **s):
# #         self.s=s
# #         print(self.s, self.a, self.b)


# # h1=Human()
# # h1.walk("arm",'leg')
# # h1.show()
# # h1.display(a=10,b=20,c=30,d=40)

# def home():
    
# home()












# # class Human:
# #     eyes=2
# #     ears=2
# #     nose=1
# #     mouth=1
# # h1=Human()
# # h1.tooth=32               Adding new attribute using object into the class
# # print(h1.tooth)

# # class Human:
# #     eyes=2
# #     ears=2
# #     nose=1
# #     mouth=1
   
# #     def show(self):          
# #         print("hello world")
# # h1=Human()
# # # h2=Human()
# # print(h1.eyes)
# # h1.show()  

# # self===represents current object
# # # self----instance variable/object variable













# # # #  Adding method in a class with keyword or parameter: 'self' - refers current object/instance (h2)
# # # #                  
# # # # # Calling method(function) using object(h1)

# # class Human:
# #     eyes=2
# #     ears=2
# #     nose=1
# #     mouth=1
# #     # Passing a value in method(function)
# #     def show(self,a):         
# #         print(a,'hello')    
# # h1=Human()
# # print(h1.eyes)
# # h1.show("God")    

# # Passing value in one function to other using self.value, 
# # thus, inclusing value in current object(h1), thus can use in any other method in this 
# # here, converted 'a' as an instance variable in the current object(h1)
# # class Human:
# #     eyes=2
# #     ears=2
# #     nose=1
# #     mouth=1
# #     def show(self,a):     
# #         self.a=a       
# #         print(self.a)
# #     def display(self):
# #         print(self.a,"hai")   
# #     def mine(self,b):
# #         self.b=b
# #         print("hello",self.a,b)
# #     def my(self):
# #         print(self.b)    
# # h1=Human()
# # print(h1.eyes)
# # h1.show("God")
# # h1.display()
# # h1.mine("Hoi")
# # h1.my()   


# # class Student:
# # #     def __init__(self, name, age):
# # #         self.name = name  # Initialize the name attribute
# # #         self.age = age    # Initialize the age attribute
# # #         print(f"Student created: {self.name}, Age: {self.age}")

# # # stud1 = Student("John", 20)

# # # When you use self.name instead of just name, you're telling Python that name is an instance attribute, 
# # # meaning each object of the class will have its own name value. Without self, 
# # # the variable would only exist within the scope of the __init__ method and wouldn’t be accessible to other methods or outside of the constructor.
# # # elf.name ensures that the variable name becomes an instance attribute, accessible throughout the class.
# # # Without self, the name variable would be just a temporary local variable, 
# # # limited to the __init__ method.

# # # class Addition:
# # #     def display(self,a,b):
# # #         self.a=a
# # #         self.b=b
# # #     def add(self):
# # #         self.c=self.a + self.b
# # #         print("addition done")
# # #     def print(self):
# # #         print(self.c)
# # # num1=int(input("Enter first number: "))   
# # # num2=int(input("Enter second number: ")) 
# # # a1=Addition()
# # # a1.display(num1,num2)
# # # a1.add()
# # # a1.print()


# # class Calculator:
# #     def display(self,a,b):
# #         self.a=a
# #         self.b=b
# #     def add(self):
# #         self.c=self.a + self.b
# #         print(self.c)
# #     def sub(self):
# #         self.d=self.a - self.b
# #         print(self.d)
# #     def mul(self):
# #         self.e=self.a * self.b
# #         print(self.e)
# #     def div(self):
# #         self.f=self.a / self.b
# #         print(self.f)
# # num1=int(input("Enter first number: "))
# # num2=int(input("Enter second number: "))
# # a1=Calculator()
# # a1.display(num1,num2)
# # a1.add()
# # a1.sub()
# # a1.mul()
# # a1.div()



# class Bankaccount:
#     def __init__(self):
#         self.a = 0  
#         self.b = 0  

#     def amount_to_deposit(self, amount):
#         self.a += amount
#         print(f"Amount deposited: {amount}")

#     def withdraw(self, amount):
#         if amount > self.a:
#             print("Insufficient balance.")
#         else:
#             self.a -= amount
#             print(f"Amount withdrawn: {amount}")

#     def balance(self):
#         print(f"Balance amount: {self.a}")

# b1 = Bankaccount()

# while True:
#     x = input("What do you want to do?: \n1. Deposit \n2. Withdraw \n3. Balance enquiry \n4. Exit\n select your choice")

#     if x == '1':  
#         amount = int(input("Enter amount to deposit: "))
#         b1.amount_to_deposit(amount)

#     elif x == '2':  
#         amount = int(input("Enter amount to withdraw: "))
#         b1.withdraw(amount)

#     elif x == '3':  
#         b1.balance()

#     elif x == '4': 
#         print("Exit process and return card.")
#         break

#     else:
#         print("Invalid option, please try again.")

# oops--object oriented programming

# 

#                                             # OOPS INHERITANCE, ENCAPSULATION, POLYMORPHYSM, ABSTRACTION

# # class Student:             Usual class function:
# #     def show(self):
# #         print("hello world")
# # stud1=Student()
# # stud1.show()







# oops---object oriented programming --class, object, attribute, method

# method---function, attributes--variables, objects--b1, n1, class--className
# def show():
#     pass
# show()

# s=10
# d='hello'
# self--instance variable/object variable
# constructor, destructor
#

# class className:

#     def __init__(self):
#         print('haiiiiiiiii')


#     s=20
#     j='hello'
#     h=[1,2,3,'hai']

#     def new(self, a, b):
#         print('function response', a+b)

#     def __del__(self):
#         print('destructor activated')
# b1=className()
# n1=className()

# print(b1.s)
# print(n1.j)
# b1.new(10,20)
# b1.k=(100,200,300)
# n1.n='python'

# print(b1.k)
# print(n1.n)

# del b1
# print(b1.j)




















#                                         #    CONSTRUCTORS
# # Constructor--- framed, as soon as object (stud1) is created, works with out calling 
# # the fucntion, as usual.
# # In Python, a constructor is a special method used to initialize objects when they are created. 
# # The constructor in Python is defined by the __init__ method. 
# # The purpose of a constructor is to set up the initial state of an object by assigning values 
# # to its attributes or performing any setup actions required.

# # what is self? ---
# # self is a reference to the current instance of the class. 
# # It is used to access variables and methods that belong to the instance.

# # class Student:
# #     count=50
# #     skin="brown"

# #     def show(self, a,b):
# #         self.a=a
# #         self.b=b
# #         print("hiiiiii")
# #         print(a)

# #     def display(self):
# #         print(self.a)

# #     def sum(self):
# #         self.c=self.a + self.b
# #         print(self.c)
        

# # stud1=Student()
# # stud1.show(10, 20)
# # stud1.display()
# # stud1.sum()



# # class Student:
# #     def __init__(self):    
# #         print("haoiiiiiiii")


# #     def show(self):
# #         print("hai")

# # stud1=Student()
# # stud1.show()

# class Student:
#     def __init__(self, a, b):
#         print("constructor created", a+b)

#     def __del__(self):
#         print("destrcutor created")

#     def show(self):
#         print("hai")

# s1=Student(10,20)
# del s1
# s1.show()


            #  Using ___init___, we can operate this operation(addition) without calling it. Here passed values to object in class and put variables in class.
# stud1=Student(10, 20)


# # class Student:
# #     def __init__(self, a, b): 
# #         self.a=a
# #         self.b=b
# #         self.c=self.a+self.b
# #         print("hello hai",self.c) 
# #     def show(self,d):
# #         print("Anjali Shyju",d, self.c)
# # stud1=Student(10,20)
# # stud1.show("hai")       

# # # Input values through __init__, add by a function and view result by another function

# class Addition:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.c=self.a+self.b
#     def result(self):
#         print("sum of number is: ",self.c)
# f=int(input('Enter first number: '))
# s=int(input('Enter second number:'))
# add1=Addition(f,s)
# add1.sum()
# add1.result()


# method over riding
# class Parent:
#     def __init__(self):
#         print('parent constructor')
#     def new(self):
#         print('hello parent')
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print('child constructor')
#     def new(self):
#         super().new()
#         print('hello child')

# c1=Child()
# c1.new()







# #                                     # Another Way ------Giving direct values
# # class Addition:
# #     def __init__(self,a,b):
# #         self.a=a
# #         self.b=b
# #     def sum(self):
# #         self.c=self.a+self.b
# #     def result(self):
# #         print("sum of number is: ",self.c)

# # # add1=Addition(10,20)
# # # add1.sum()
# # # add1.result()

# # # class Addition:
# # #     def __init__(self,a,b):
# # #         self.a=a
# # #         self.b=b
# # #     def sum(self):
# # #         self.c=self.a+self.b
# # #     def result(self):
# # #         print("sum of number is: ",self.c)

# # # add1=Addition(10,20)
# # # add1.sum()
# # # add1.result()
# # # del add1
# # # add1.show()

# #                                     # DESTRUCTOR----Formed while a class is deleted
# class Student:
#     eyes=2
#     def __init__(self, a, b):
#         self.a=a
#         self.b=b
#         self.c=self.a+self.b
#         print("hello hai",self.c) 
#     def show(self):
#         print("Anjali Shyju")
#     def __del__(self):
#         print("destructor")
   
# stud1=Student(10,20)
# stud1.show()  
# del stud1
# print(stud1.eyes)



# write a python program to get even numbers greater than 12 from a range of numbers 10-100

# write a python prograam to take count of vowels in a sentence
g='Hello dear Arya, could you please help me out?'

# write a python program to check whether a string is having more than 5 characters or not















# # # class Student:                As soon as keyword'del'is called moving to function __del__, thus not working remaining functions.
# # #     def __del__(self):
# # #         print("destructor")
# # #     def __init__(self, a, b):
# # #         self.a=a
# # #         self.b=b
# # #         self.c=self.a+self.b
# # #         print("hello hai",self.c) 
# # #     def show(self):
# # #         print("Anjali Shyju")
# # # stud1=Student(10,20)
# # # del stud1
# # # stud1.show()  

# # # properties-----inheritance, abstraction, encapsulation, polymorphism
# # # Inheritance

# # #  Single Inheritance - Inherited functions in class Parent to Child
# # # parent-superclass, childclass- subclass

# class Parent:
#     salary=12000
#     def work(self):
#         print("working ability")
# class Child(Parent):
#     def study(self):
#         print("learning ability")

# c1=Child()
# c2=Child()
# c1.study()
# c1.work()
# print(c1.salary)
# print(c2.salary)

# # multiple inheritance
# class Father:
#     def work(self):
#         print("working ability")
# class Mother:
#     def cook(self):
#         print("cooking tasty")
# class Child(Father, Mother):
#     def study(self):
#         print("studying")
# c1=Child()
# c1.study()
# c1.work()
# c1.cook()




# # # multiple inheritance

# # class Father:
# #     def work(self):
# #         print("working")
# # class Mother:
# #     def cook(self):
# #         print("cooking")
# # class Child(Mother, Father):
# #     def study(self):
# #         print("studying")
        
# # c=Child()
# # c2=Child()
# # c.cook()
# # c.study()
# # c.work()




# #                     # Multilevel-Inheritance

# class Grandfather:
#     def walk(self):
#         print("walking")
# class Father(Grandfather):
#     def work(self):
#         print("working")
# class Child(Father):
#     def study(self):
#         print("studying")
# c=Child()
# c.work()
# c.study()
# c.walk()
# #             # hyrarcial inheritance ( one parant and multiple child)

# class School:
#     def manage(self):
#         print("management")
# class Teacher1(School):
#     def teach(self):
#         print("teaching subjects")
# class Teacher2(School):
#     def music(self):
#         print("teaching music")
# class Student(Teacher1,Teacher2):
#     def learn(self):
#         print("learning")
# s=Student()
# s.learn()
# s.teach()
# s.music()
# s.manage()





# # # class Parent:
# #     def work(self):
# #         print('working')
# # class Child1(Parent):
# #     def study(self):
# #         print("studying")
# # class Child2(Parent):
# #     def music(self):
# #         print("learn music")
# s1=Child1()
# s2=Child2()
# s1.study()
# s1.work()
# s2.music()
# s2.work()


            # magic methods or dunder methods
# In Python, dunder methods (also known as magic methods) are special methods that have double underscores (__) at the 
# beginning and end of their names. These methods are used to define the behavior of objects when certain operations 
# (like addition, subtraction, or printing) are performed. 
# For example, __init__, __add__, __str__, etc., are dunder methods.
# class A:
#     def __init__(self, a):
#         self.a = a
#         print(self.a)

#     def __add__(self, other):
#         return self.a + other.a  # This returns the sum of the 'a' attributes

# __init__(self, a): This is the constructor method. It is called when a new object of class A is created. 
# It takes one argument, a, and assigns it to the self.a attribute of the object. Then, it prints self.a.

# When you create an object like obj1 = A(2), the __init__ method is called, and it sets self.a to 2 and prints 

# __add__(self, other): This is a magic method for defining the behavior of the + operator for objects of class A. 
# When you try to add two objects (e.g., obj1 + obj2), Python will call the __add__ method to determine 
# what the result of the addition should be.

# self.a + other.a: This returns the sum of the a attributes from self (the left-hand object) and 
# other (the right-hand object in the addition).



# class A:
#     def __init__(self,a):
#         self.a=a
              
#         print(self.a)
#     def __add__(self,other):
#         return self.a           
#         return other.a
#         return other.a
#         return self.a+other.a
# obj1=A(2)
# a1=A(3)
# a2=A(4)

# obj2=A(3)


# class A:
#     def __init__(self,a):
#         self.a=a       
#         print(self.a)
#     def __add__(self,other):
#         return self.a+other.a
#     def __sub__(self,other):
#         return self.a-other.a
#     def __mul__(self,other):
#         return self.a*other.a
#     def __truediv__(self,other):
#         return self.a/other.a
#     def __floordiv__(self,other):
#         return self.a//other.a
#     def __pow__(self,other):
#         return self.a**other.a
#     def __mod__(self,other):
#         return self.a%other.a
#     def __lt__(self,other):
#         return self.a<other.a
#     def __gt__(self,other):
#         return other.a>self.a
#     def __eq__(self,other):
#         return self.a!=other.a
# obj1=A(2)
# obj2=A(3)
# print(obj1+obj2)
# print(obj2-obj1)
# print(obj1*obj2)
# print(obj2/obj1)
# print(obj2//obj1)
# print(obj2**obj1)
# print(obj2%obj1)
# print(obj1<obj2)
# print(obj2>obj1)
# print(obj1!=obj2)

# class Adding:
#     def __add__(self,other):
#         print(self.n)
#         print(other.n)
#         return Adding(self.n+other.n)
# a1=Adding(2)
# a2=Adding(3)
# a3=Adding(4)
# result=a1+a2+a3
# print(result.n)
# x=isinstance(a1,Adding)
# print(x)

            # method over riding

# class A:
#     def play_function(self):
#         print("playing")
# class B(A):
#     def play_function(self):
#         print("PLAYING")
# obj=B()
# obj.play_function()




# class A:
#     def play(self):
#         print("working")
# class B(A):
#     def play(self):
#         super().play()
#         print("PLAYING")
# obj=B()
# obj.play()

#             # constructor over riding 

# class A:
#     def __init__(self):
#         print("class a")
#     def play(self):
#         print("playing")
# class B(A):
#     def __init__(self):
#         print("class b")
#     def play(self):
#         print("PLAYING")
# obj=B()
# obj.play()


# class A:
#     def __init__(self):
#         print("class a")
#     def play(self):
#         print("playing")
# class B(A):
#     def __init__(self):
#         print("class b")
#         super().__init__()
#     def play(self):
#         super().play()
#         print("PLAYING")
# obj=B()
# obj.play()

# polymorphism

# # class A:
# #     def __init__(self):
# #         print("class a")
# #     def play(self):
# #         print("playing")
# # class B(A):
# #     pass
# # obj=B()
# # obj.play()


# #                                        private methods

# # class A:
# #     a=10
# #     def study(self):
# #         print("studying")
# # obj=A()
# # obj.study()
# # print(obj.a)

# # class A:
# #     def __study(self):
# #         print("studying")
# # obj=A()
# # obj.__study()

# # class A:
# #     def __init__(self):
# #         self.__study()
# #     def __study(self):
# #         print("studying")
# # obj=A()


# # class A:
# #     __a=10
# #     def __init__(self):
# #         self.__study()
# #         print(A.__a)
# #     def __study(self):
# #         print("studying")
# # obj=A()

# # class A:
# #     __a=10
#     def __init__(self):
#         self.__study()
#         print(A.__a)
#     def __study(self):
#         print("studying")
# obj=A()
# print(obj._A__a)
                            #    protect methods   mathod called inside function or child function, using constructor



# class Parent:
#     _name="Anjali"
#     def _study(self):
#         print("studying")
# class Child(Parent):
#     def __init__(self):
#         self._run()
#         self._study()
#         print(self._name)
#     def _run(self):
#         print("running)")
# c=Child()

# Encapsulation - overloading and over riding - access methods inside function only
# access speciyiers -  private, public, protected
# polymorphism - 

# PHONE BOOK USING OOPS

# class Adddetails:
#     def add_phn(self):
#         self.phone=int(input("enter a number: "))
#         self.phone_list=[]
#         add_ph=True
#         self.phone_list.append(self.phone)
#         while add_ph:
#             ph_ch=input("add another number? type 'Y' OR 'N' : ").upper()
#             if ph_ch=='Y':
#                 alt_ph=int(input("enter a number: "))
#                 self.phone_list.append(alt_ph)
#             else:
#                 add_ph=False
#         return self.phone_list
#     def add_email(self):
#         self.email=input("enter a email: ")
#         self.email_list=[]
#         add_em=True
#         self.email_list.append(self.email)
#         while add_em:
#             em_ch=input("add enother email? type 'Y OR 'N' :").upper()
#             if em_ch=='Y':
#                 alt_em=input("enter email: ")
#                 self.email_list.append(alt_em)
#             else:
#                 add_em=False
#         return self.email_list

# class PhoneBook:
#     contacts={}
#     def __init__(self,name,address,emaillist,phnlist):
#         self.u_name=name
#         self.address=address
#         self.email=emaillist
#         self.phone=phnlist
#     def add_contacts(self):
#         self.contacts[self.u_name]= {"name":self.u_name,"address":self.address,"email":self.email,"phnnumber":self.phno}
#         print("contact added successfully")
#     def updatecontacts(self, name):
#         if name in self.contacts:
#             print("1.Update name: ")
#             print("2.Update address: ")
#             print("3.Update email: ")
#             print("4.Update phn number: ")
#             print("5.exit updation of contacts: ")
#             choice=int(input("enter your choice: "))
#             if choice ==1:
#                 newname=input("enter new name for the conatct")
#                 self.contacts[newname]= self.contacts.pop(name)
#                 self.contacts[newname]["name"]=newname
#                 print("updated name succesfully")
#             elif choice==2:
#                 newaddress=input("enter new address for the conatct")
#                 self.contacts[name]["address"]=newaddress
#                 print("updated address succesfully")
#             elif choice==3:
#                 emaillist=self.contacts[name]["email"]
#                 if len(emaillist)>0:
#                     for i in range (len(emaillist)):
#                         ch=input(f"{emaillist[i]} update? Type 'Y' OR 'N': ").upper()
#                         if ch=='Y':
#                             NewEmail=input("enter new email: ")
#                             emaillist[i]=NewEmail
#                             print("updated email successfully")
#                 else:
#                     ad = Adddetails()
#                     emaillist=ad.add_email()
#                     self.contacts[name]["email"]=emaillist
#                     print("added email successfully")
#             elif choice==4:
#                 phnnumberlist=self.contacts[name]["phnnumber"]
#                 if len(phnnumberlist)>0:
#                     for i in range(len(phnnumberlist)):
#                         fn=input(f"{phnnumberlist[i]} update? Type 'Y' OR 'N': ").upper()
#                         if fn=='Y':
#                             Newphnnumber=input("enter new number: ")
#                             phnnumberlist[i]=Newphnnumber
#                             print("updated new phnnumber successfully")
#                 else:
#                     phnnumberlist=ad.add_phn()
#                     self.contacts[name]["phnnumber"]=phnnumberlist
#                     print("added phnnumber successfully")
#             else:
#                 print("updation finished")
#     def view_contacts(self,name):
#         if name in self.contacts:
#             print(self.contacts[self.u_name])

#     def view_all_contacts(self):
#         print(self.contacts())

#     def delete_contact(self,name):
#         if name in self.contacts:
#             print("1.Delete address: ")
#             print("2.Delete email: ")
#             print("3.Delete phn number: ")
#             print("4.Delete name")
#             choice=int(input("enter your choice: "))
#             if choice ==1:
#                 del self.contacts['address']
#                 print("deleted address succesfully")
#             elif choice==2:
#                 emaillist=self.contacts["email"]
#                 if len(emaillist)>0:
#                     for i in range (len(emaillist)):
#                         ch=input(f"{emaillist[i]} delete? Type 'Y' OR 'N': ").upper()
#                         if ch=='Y':
#                             del self.contacts[emaillist[i]]
#                             print("deleted email successfully")
#                 else:
#                     print("no email to delete")
#             elif choice==3:
#                 phnnumberlist=self.contacts[name]["phnnumber"]
#                 if len(phnnumberlist)>0:
#                     for i in range(len(phnnumberlist)):
#                         fn=input(f"{phnnumberlist[i]} update? Type 'Y' OR 'N': ").upper()
#                         if fn=='Y':
#                             del self.contacts[phnnumberlist[i]]
#                             print("deleted phnnumber successfully")
#                 else:
#                     print("no phn number to delete")
#             elif choice==4:
#                 del self.contacts [name]
#                 print("name deleted successfully")
# choice=int(input("1.Add contacts \n2.Update contacts \n3.View  all contacts \n4.View contact \n5.Delete contacts \n enter your choice: "))
# m=True
# while m:
#     if choice==1:
#         name=input("enter the name to add:")
#         address=input("enter the address to add: ")
#         detail=Adddetails()
#         emaillist=detail.add_email()
#         phnlist=detail.add_phn()
#         obj=PhoneBook(name,address,emaillist,phnlist)
#         obj.add_contacts()
#         choice=int(input("1.Add contacts \n2.Update contacts \n3.View  all contacts \n4.View contact \n5.Delete contacts \n enter your choice: "))
#     elif choice==2:
#         name_to_update=input("enter name to update: ")
#         obj=PhoneBook(name,address,emaillist,phnlist)
#         obj.updatecontacts(name_to_update)
#         choice=int(input("1.Add contacts \n2.Update contacts \n3.View  all contacts \n4.View contact \n5.Delete contacts \n enter your choice: "))
#     elif choice==3:
#         obj=PhoneBook(name,address,emaillist,phnlist)
#         obj.view_all_contacts()
#         choice=int(input("1.Add contacts \n2.Update contacts \n3.View  all contacts \n4.View contact \n5.Delete contacts \n enter your choice: "))
#     elif choice==4:
#         view=input("enter contact name to view: ")
#         obj.view_contacts(view)
#         choice=int(input("1.Add contacts \n2.Update contacts \n3.View  all contacts \n4.View contact \n5.Delete contacts \n enter your choice: "))
#     elif choice==5:
#         del_name=input('enter name to delete: ')
#         obj.delete_contact(del_name)
#         choice=int(input("1.Add contacts \n2.Update contacts \n3.View  all contacts \n4.View contact \n5.Delete contacts \n enter your choice: "))
#     else:
#         print("exit")


    









# inbuilt modules

# import math
# print(math.factorial(5))
# print(math.pow(3,7))
# print(math.lcm(20,30,40))
# print(math.ceil(.2))
# print(math.floor(.2))

# from math import factorial,pow
# print(factorial(5))

# # from math import *

# import datetime

# x=datetime.datetime.now()
# print(x)
# # # # strf- string format value ---human readable form
# print(x.strftime("%B"))
# print(x.strftime('%b'))

# print(x.strftime('%Y'))
# print(x.strftime('%y'))


# print(x.strftime('%A'))
# print(x.strftime('%a'))


# print(x.strftime('%d'))
# print(x.strftime('%m'))


# import random
# d=[10,20,30]
# d.random.shuffle()
# print(d)


                                                # Encapsulation
# Encapsulation is a concept in object-oriented programming (OOP) that refers to bundling data (variables) and methods (functions) that operate on that data into a single unit, typically a class. 
# The key aspect of encapsulation is data hiding, 
# which ensures that the internal state of an object is protected from unintended interference by external code. 
# This protection is achieved by controlling access to the object's attributes and methods.

# Access Modifiers
# Access modifiers in OOP control the visibility and accessibility of class members (attributes and methods). 
# While different languages implement access modifiers in different ways, Python uses conventions to achieve similar results.

# Python has three main types of access modifiers:

# Public: Accessible from anywhere (within and outside the class).
# Protected: Accessible within the class and its subclasses.
# Private: Accessible only within the class.



# class Student:
#     eyes=2
#     def show():


# obj=Student()
# obj.show()
# print(obj.eyes())

# oops---inheritance, abstraction, encapsulation  (encapsulation, hide)


# ENCAPSULATION----------ACCESS MODIFY/CONTROL
# In Object-Oriented Programming (OOP), methods (and variables) can have different levels of access control, typically referred to as private, protected, and public. These access specifiers define 
# how and where class members (methods and variables) can be accessed from within or outside the class.
# Public Methods
# Accessibility: Can be accessed from anywhere, both inside and outside the class.
# Syntax: Methods are public by default unless specified otherwise.
# Use case: Public methods are used when you want the functionality to be available for everyone.


# public, private, protected --access modifers

# class MyClass:
#     def public_method(self):
#         print("This is a public method.")
#     def show(self):
#         print("hello")

# obj = MyClass()
# v1=MyClass()
# obj.public_method()
# obj.show()


# # Private Methods
# # Accessibility: Can only be accessed within the class itself. They are not accessible from outside the class.
# # Syntax: By prefixing the method name with two underscores (__), it becomes private.
# # Use case: Private methods are used when you want to hide the internal implementation details and prevent external access.

# class MyClass:
#     def __privatemethod(self):
#         print("helloooooooo")

#     def publicfunction(self):
#         self.__privatemethod()
#         print("response of public function")


# b1=MyClass()
# # b1.__privatemethod()
# b1.publicfunction()

# encapsulation--encapsulate+ security
# access modifiers -- public, private, protected

# # Protected Methods
# # Accessibility: Can be accessed within the class and its subclasses but not from outside the class. In Python, protected members are conventionally indicated by a single underscore (_).
# # Syntax: Prefix the method name with a single underscore (_) to indicate it’s protected.
# # Use case: Protected methods are used when you want to allow access to subclasses but still restrict access from other external classes.

class MyClass:
    def _protected_method(self):
        print("This is a protected method.")
        
class SubClass(MyClass):
    def access_protected(self):
        self._protected_method()  

obj = MyClass()
obj._protected_method()

g=SubClass()
g.access_protected()
g._protected_method()





# class Human:
#     def _vision(self):
#         print('vision')

#     def new(self):
#         self._vision()

# class Men(Human):
#     def man_power(self):
#         print('hai')

# h1=Human()
# h1._vision()
# h1.new()

# m1=Men()
# m1._vision()
# access modifiers--public, private, protected









# # Key Differences:
# # Public: Accessible from anywhere (no leading underscore).
# # Private: Accessible only within the class (double underscore __).
# # Protected: Accessible within the class and subclasses (single underscore _), but discouraged from being accessed directly outside.


# n = int(input("enter a number: "))  
# a, b = 0, 1

# print("Fibonacci series using for loop:")
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# 0, 1, 1, 2, 3, 5, 8


# n = 10  
# a, b = 0, 1
# count = 0

# print("\nFibonacci series using while loop:")
# while count < n:
#     print(a, end=" ")
#     a, b = b, a + b
#     count += 1

# d=[]
# f=[]

# for i in range(1,11):
#     if (i%2!=0):
#         d.append(i)
#     else:
#         f.append(i)
# print(d)
# print(f)
# k=[]
# d="python program"
# for i in d:
#     if ("p" in d):
#         k.append(i)
# print(k)

# d=[10,20,30,40,50,50,50]
# count=0
# for i in d:
#     if (50 in d) :
#         count+=1
# print(count)

# first ten natural numbers ---get squares of all even nubers, cube of all odd number
# parameters
# def show(a,b):
#     print(a+b)
# show(1,2)
# arguments


# def display(a,b):
#     return a+b
# print(display(2,3))


# local variable and global variable

# d=10 global variable
# def show():
#     print(d)
# show()


# print(d)


# local variable
# def show():
#     d=10
#     print(d)
# show()

# print(d)

# def show():
#     global d
#     d=10
#     print(d)
# show()

# print(d)



# def show(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a/b)
# show(20,10)

# g=[]
# s=[1,2,3,4,5]
# # [11,12,13,14,15, 21, 22]
# for i in s:
#     for j in s:
#         g.append(i*10+j)
# print(g)

# # 11=1*10+1
# # 12=1*10+2


# d=["1","2","3","4","5"]
# for i in d:
#     for j in d:
#         print((i+j),end=" ")

#                        Standard Library Modules
# In Python, inbuilt modules (also known as standard library modules) refer to the set of 
# pre-written Python files (or libraries) that come bundled with the Python installation. 
# These modules provide a 
# wide range of functionality that you can use directly in your programs without needing 
# to install anything extra.


# To use an inbuilt module, 
# you typically need to import it at the beginning of your Python script using the import keyword

# d=[10,20,30]
# print(sum(d))

# import math
# print(math.factorial(5))
# print(math.pow(6,3))
# print(math.lcm(2,3,4,5))
# print(math.ceil(1.2))
# print(math.floor(1.2))

# from math import factorial
# print(factorial(5))

# from math import *
# print(factorial(5))
# print(pow(3,2))
# print(lcm(2,3,4,5))
# print(ceil(1.2))
# print(floor(1.2))

import random
# p=[10,20,30,40,50]
# random.shuffle(p)
# print(p)
# print(random.choices(p))
# print(random.sample(p, 4))


# print(random.randint(1,20))

# print(random.randrange(1,11, 3))


# import datetime
# p=datetime.datetime.now()
# print(p)

# # # # # # strf time---string format time
# print(p.strftime("%Y"))
# print(p.strftime("%y"))

# print(p.strftime("%B"))
# print(p.strftime("%b"))

# print(p.strftime("%A"))
# print(p.strftime("%a"))

# print(p.strftime("%m"))
# print(p.strftime("%d"))






# # factorial  5=5 x 4 x 3 x 2 x1 
# # n=int(input("enter a number: "))
# # fact=1
# # for i in range(1,n+1):
# #     fact*=i
# # print(fact,"is the factorial of the number",n)


# # n=int(input("enter a number: "))
# # count=1
# # fact=1
# # while (count<=n):
# #     fact*=count
# #     count+=1
# # print(fact,"is the factorial of the number",n)






# # class Mainclass:

# #     def method1():
# #         pass

# #     def __method2():
# #         pass

# #     def _method3():
# #         pass


# # obj=Mainclass()



# # print("helo")


# # d={'name':"ammu", 'age':10}

# # def calculator(num1, num2, operator):
# #     if operator == '+':
# #         return num1 + num2
# #     elif operator == '-':
# #         return num1 - num2
# #     elif operator == '*':
# #         return num1 * num2
# #     elif operator == '/':
# #         return num1 / num2 if num2 != 0 else 'Division by zero error'
# #     else:
# #         return 'Invalid operator'





# import random 
# lottery_ticketslist=[]
# for i in range(100):
#     lottery_ticketslist.append(random.randint(100000,999999))
# win=random.sample(lottery_ticketslist,2)
# print("winners are",win)

# import random
# win=5
# attempt=1
# while attempt<=3:
#     number=random.randint(0,5)
#     print(number)
#     if number==win:
#         print("You won")
#         break
#     else:
#         attempt+=1
#         print("You lost")
# else:
#     print("Game Over")

# class Human:
#     head=1

#     def __init__(self,a):
#         print("constructor evoked",a)

#     def vision(self,c, d):
#         self.c=c
#         self.d=d
#         print("see")

#     def show(self):
#         print(self.c + self.d)

    # def __del__(self):
        # print("deleted")



# h1=Human(10)
# h1.vision(20,30)
# # del h1
# h1.show()


# functions---
# syntax

# def functionname(a):
#     pass
# functionname(10)
# 10---argument
# a----parameter

# def show(a, ):
    # print(a)
    # print(a+b)
# d="hello"
# show(10,20)
# show(d)


# def show(a):
#     for i in a:
#         if (i%2==0):
#             print(i)

# show([10,20,30, 21, 31])


# arbitrary argument (*args)
# def show(*a):
#     print(a)
# show(10,20, 30, 40,"hello",[20,30])


# keyword argument(kwargs)
# def display(place,age,name):
    # print(place,age,name)
    
# display(name="arya",age=10,place="tvm")

# arbitrary keyword argumnet (**kwargs)
# def display(**k):
#     print(k)
    
# display(name="arya",age=10,place="tvm")/


# def factorial(n):
#     fact=1
#     sum=0
#     for i in range(1,n+1):
#         fact*=i
#         sum+=i
#     print(fact)
#     print(sum)
# num=int(input("enter a number: "))
# factorial(num)



# def factorial(n):
#     fact=1
#     sum=0
#     for i in range(1,n+1):
#         fact*=i
#         sum+=i
#     print(fact)
#     print(sum)
# num=int(input("enter a number: "))
# factorial(num)


