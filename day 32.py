# #                                         # Attributes in OOPS ----GET, HAS, SET, DEL

# class Student:
#     name="Devika"
#     age="25"
# obj=Student()
# # # obj.address='tvm'

# # obj.teeth=32


# print(obj.name)
# # # print(obj.age()

# print(getattr(obj,'name'))
# print(hasattr(obj,'name'))

# print(setattr(obj,'address','kochi'))

# print(hasattr(obj,'address'))
# # print(hasattr(obj,'address'))
# # # print(getattr(obj,'address'))

# # # # # # # # # # # print(setattr(obj,'name','Veena'))
# # # print(hasattr(obj,'address'))
# # # print(getattr(obj,'address'))

# print(delattr(obj,'name'))
# print(hasattr(obj,'name'))
# # print(delattr(obj,'address'))
# print(hasattr(obj,'address'))



# constructor ---__init__
# class Human:
#     eyes=2

#     def __init__(self, a, b):
#         print("constructor formed",a+b)
#     def __del__(self):
#         print("destructor generated")
    
# h1=Human(10,20)
# del h1
# print(h1.eyes)







                                                        # ABSTRACTION

# Abstraction in Object-Oriented Programming (OOP) is a concept that focuses on hiding the complex implementation details of a system while exposing only the necessary, high-level functionalities. It allows developers to work with objects at a more conceptual level without worrying about the underlying complexity.

# Key aspects of abstraction:
# Hides Implementation: Abstraction conceals the internal workings of objects and exposes only what is relevant to the outside world.
# Simplifies Interaction: By focusing on what an object does rather than how it does it, abstraction simplifies code and improves clarity.
# Defines Interfaces: In OOP, abstraction is often achieved through abstract classes and interfaces, which define the structure without providing implementation.

# In Python, ABC, abc, and @abstractmethod are part of the abstract base class mechanism, which allows for the creation of abstract classes and methods. These tools enforce certain design patterns and allow the implementation of abstraction in object-oriented programming.

# 1. ABC (Abstract Base Class)
# ABC is a class from the abc module in Python that is used as a base class for creating abstract classes. An abstract class is one that cannot be instantiated directly and often contains one or more abstract methods (methods without implementations). It is used to define a blueprint for other classes.

# Purpose: ABC allows a class to serve as a template for derived classes, ensuring that the derived classes implement specific methods.

# The abc module stands for Abstract Base Classes. It provides the infrastructure for defining abstract base classes and abstract methods in Python.

# Purpose: It enables the creation of abstract base classes that cannot be instantiated directly but can be subclassed by other classes that provide concrete implementations for the abstract methods.
# 3. @abstractmethod
# @abstractmethod is a decorator from the abc module that marks a method as abstract. An abstract method is one that must be implemented by any non-abstract subclass. If a class contains one or more abstract methods, it cannot be instantiated until all the abstract methods are implemented by its subclasses.

# Purpose: @abstractmethod forces subclasses to provide concrete implementations of the abstract method, ensuring that they adhere to the interface defined in the abstract class.


# 

# # decorator
# from abc import ABC, abstractmethod
 
# class Bankaccount(ABC):
#     pass
    
#     def __init__(self,account_number,current_balance=0):
#         self._account_number=account_number
#         self._current_balance=current_balance

#     @abstractmethod
#     def deposit(self,amount):
#         pass
#     @abstractmethod
#     def withdraw(self,withdraw):
#         pass

#     def account_number(self):
#         return self._account_number
    
#     def current_balance(self):
#         return self._current_balance
    
# class Savings_account(Bankaccount):
#     pass
#     def deposit(self,amount):
#         if amount>0:
#             self._current_balance+=amount
#             print("Account balance after deposit is: ",self._current_balance)
#         else:
#             print("invalid amount deposited")
#     def withdraw(self,amount):
#         if amount>0 and amount<=self._current_balance:
#             self._current_balance-=amount
#             print("Account balance after withdrawal is: ",self._current_balance)
#         elif amount<=0:
#             print("invalid command, amount to withdraw should be greater than zero")
#         elif amount>=self._current_balance:
#             print("amount to withdraw should not be greater than current balance")


# ac=int(input("enter account number: "))


# sa=Savings_account(ac)

# while True:
#     x=int(input("what you want to do? \n1.Get account number\n2.check current balance\n3.deposit amount\n4.withdraw amount\n5.Exit \n enter your choice"))
#     if x==1:
#        print("Account number is: ",sa.account_number())
#     elif x==2:
#        print("current balance is: ", sa.current_balance())
#     elif x==3:
#         deposit_amount=int(input("enter amount to deposit: "))
#         sa.deposit(deposit_amount)
#     elif x==4:
#         withdraw_amount=int(input("enter amount to withdraw: "))
#         sa.withdraw(withdraw_amount)
#     elif x==5:
#         print("Thank you for choosing ABC bank, please take your card")
#         break
#     else:
#         print('invalid option')

# # class Parent():
# #     def home(self):
# #         print("hav home")

# # class Child(Parent):
# #     def study(self):
# #         print('hav learning ability')

# # sa=Child()
# # sa.home()





from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

circle = Circle(5)  # Circle with radius 5
rectangle = Rectangle(4, 6)  # Rectangle with width 4 and height 6

print(f"Circle: Area = {circle.area()}, Perimeter = {circle.perimeter()}")
print(f"Rectangle: Area = {rectangle.area()}, Perimeter = {rectangle.perimeter()}")

# primary, collection, string, if, elif,else, for loop, while , prime , amstriong, palindrome


#                                                         # class method

# # class Human:
# #     eyes=2
# #     def show(self):
#         print("hello")
# h1=Human()
# print(h1.eyes)
# h1.show()




# class Myclass:
#     class_variable=0

#     @classmethod
#     def increment_class_variable(cls,increment):
#         cls.class_variable += increment

# obj1=Myclass()
# obj2=Myclass()

# Myclass.increment_class_variable(10)

# print(obj1.class_variable)
# print(obj2.class_variable)

                            # class method and static method
# CLASS METHOD
# Decorator: @classmethod
# First Parameter: The first parameter of a class method is cls, which refers to the class itself (not the instance/object).
# Purpose: Class methods can access and modify class-level attributes. They are used when you need to do something related to the class as a whole rather than any particular instance.
# Calling: Can be called on the class itself or on an instance of the class.
# 


# class MyClass:
#     v=0
#     @classmethod
#     def new_function(cls, m):
#         cls.v+=m
#         print(cls.v)

# MyClass.new_function(100) 
# print(MyClass.v)  

# obj=MyClass()
# obj.new_function(20)
# print(obj.v)





# STATIC METHOD

# Decorator: @staticmethod
# First Parameter: Static methods don't take self or cls as the first parameter, meaning they 
# don't have access to instance-specific or class-specific data.
# Purpose: Static methods are used when you want a method that doesn't need to 
# access class or instance attributes. It behaves like a regular function but is logically grouped within the class.
# Calling: Like class methods, static methods can also be called on both 
# the class and instances, but they neither modify class state nor instance state.

# class MyClass:
#     v=12

#     @staticmethod
#     def static_method(x, y):
#         return x + y

# print(MyClass.static_method(5, 6))  
# obj = MyClass()
# print(obj.static_method(7, 8))      




#  # static method


# class Myclass:

#     @staticmethod
#     def static_method(x,y):
#         return x+y
# print(Myclass.static_method(5,6))
    
        #    OR
# class Myclass:
#     @staticmethod
#     def static_method(a,b):
#         print(a-b)
# Myclass.static_method(6,1)
         

# class Student:
#     @staticmethod
#     def sum(a,b):
#         print(a+b)
#     @staticmethod
#     def sub(x,y):
#         print(x-y)
# obj=Student()
# obj.sum(6,5)
# obj.sub(10,5)

#    OR
# Student.sum(6,5)
# Student.sub(10,5)

                                                    # DESTRUCTOR

# class Student:
#     a="Vishnu"
#     def __init__(self,name):
#         self.name=name
#         print("constructor created")

#     def __del__(self):
#         print("deleting everything")

# obj=Student("Anjali")



# print(obj.name)
# print(obj.a)
# del obj
# print(obj.name)
# print(obj.a)


# for i in range(1,10):
#     print(j)


#  print("hello world")


            #   EXCEPTION/ERROR HANDLING
# Exception handling in Python is the process of responding to the occurrence of exceptions/errors 
# that occur during execution. Instead of the program crashing when it encounters an error, 
# you can handle exceptions gracefully using try, except, else, and finally blocks.

# a=1000
# b=a
# print(b/0)

# print("hello")

# try:
#     a=1000
#     b=a
#     print(b/0)
# except:
#     print("ZERO DIVISION ERROR")
# print("START")
# print("helooooooo")


# a=int(input("enter a number: "))
# print(a)

#                               # value error
# try:
#     a=int(input("enter your age: "))
#     print(a)
# except:
#     print("value error")

#                                # index error
# try:
#     a=[1,2,3]
#     print(a[4])
# except:
#     print("index error")

#                                   # name error
# try:
#     print(z)
# except:
#     print("name error")
# #                                   # key error
# # #
# try:
#     a={"name":"ammu","age":10}
#     print(a["place"])
# except:
#     print("key error")

       
# print("start")
#
#    
#                                   # import error
# try:
#     from math import cube
# except:
#     print("import error")
    
# print("STOP")

 
# try:
#     from math import factorial
#     print(factorial(-1))
# except:
#     print("import error")
# else:
#     print("no exceptions")

                        # FINALLY
try:
    import math
    print(math.factorial(-1))
except:
    print("import error")
else:
    print("no exceptions")
finally:
    print("finished either having an error or not ")


# try:
#     from math import factorial
# except:
#     print("import error")
# else:
#     print("no exceptions")
# finally:
#     print("finished")  
 

# try:
#     from math import math
# except ImportError:
#     print("error occured")
# except:
#     print("import error")
# else:
#     print("no exceptions")
# finally:
#     print("finished")  

                            # RAISE

# # try:
# #     age=int(input("enter the age: "))
# #     if age>18:
# #         raise
# #     else:
#         print("age is ",age)
# # except ValueError:
# #     print("value error")
# # except:
# #     print("error occured")

# try:
#     age=int(input("enter the age: "))
#     if age>18:
#         raise ValueError
#     else:
#         print("age is ",age)
# except ValueError:
#     print("value error")
# except:
#     print("error occured")

                                # ASSERT
# syntax:  assert condition, message of exception
# if condition true, execute next line of code, if false, print message given, assertion error.
# try:
#     a=5
#     b=6
#     assert a<b,"a is greater"
#     print("success")
# except AssertionError as msg:
#     print(msg)


# try:
#     a=50
#     b=6
#     assert a<b,"a is greater than b"
#     print("success")
# except AssertionError as msg:
#     print(msg)

# try:
#     a=int(input("enter a number:"))
#     # a=10
#     assert a>=0,"error occured as number is less than zero "
#     print(a*a)
# except AssertionError as msg:
#     print(msg)

                    # customize error by inheriting class Exception:
# Here, Age error is a customised error framed by inheriting the class Exception and callig that using RAISE command
# class Ageerror(Exception):
#     pass
# try:
#     age=int(input("enter your age"))
#     if age>18:
#         raise Ageerror
#     else:
#         print("age is",age)
# except Ageerror:
#     print("age should be less than 18")

# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)



# a=20
# b=30
# c=40
# d=
# print(a)
# print(b)
# print(c)
# print(d)


# from abc import ABC, abstractmethod

# class BankAccount(ABC):
#     def __init__(self, ac_num, curr_balance=100):
#         self._ac_num=ac_num
#         self._curr_balance=curr_balance

#     def get_account_number(self):
#         return self._ac_num
    
#     def get_current_balance(self):
#         return self._curr_balance
    
#     @abstractmethod
#     def depositfunction(self,deposit_am):
#         pass

#     @abstractmethod
#     def 


# class SavingsAccount(BankAccount):
#     pass

# ac_num=int(input("enter account number of user: "))

# s1=SavingsAccount(ac_num)


# sa.get_coount(number())

# sa.depositfunction()


# a = [10, 24, 76, 23, 12]
# largest = max(a)
# print(largest)

# def isPalindrome(s):
#     return s == s[::-1]
# s = "malayalam"
# ans = isPalindrome(s)

# if ans:
#     print("Yes")
# else:
#     print("No")

# num = 2
# if num > 1:
  
#     for i in range(2, (num//2)+1):
      
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
# #         print(num, "is a prime number")
# # else:
# #     print(num, "is not a prime number")



# # 1. Abstraction using an Abstract Base Class
# from abc import ABC, abstractmethod

# # Abstract class for Shape (Abstraction)
# class Shape(ABC):
#     def __init__(self):
#         # Encapsulation: private attributes for dimensions
#         self.__dimension1 = 0
#         self.__dimension2 = 0

#     # Getter method for dimension1
#     def get_dimension1(self):
#         return self.__dimension1

#     # Setter method for dimension1
#     def set_dimension1(self, dimension1):
#         self.__dimension1 = dimension1

#     # Getter method for dimension2
#     def get_dimension2(self):
#         return self.__dimension2

#     # Setter method for dimension2
#     def set_dimension2(self, dimension2):
#         self.__dimension2 = dimension2

#     # Abstract methods for area and perimeter
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def perimeter(self):
#         pass

# # 2. Inheritance: Rectangle class inherits from Shape
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__()
#         self.set_dimension1(length)  # Setting dimensions using setters
#         self.set_dimension2(width)

#     # Polymorphism: Overriding the area method
#     def area(self):
#         return self.get_dimension1() * self.get_dimension2()

#     # Polymorphism: Overriding the perimeter method
#     def perimeter(self):
#         return 2 * (self.get_dimension1() + self.get_dimension2())

# # 3. Inheritance: Circle class inherits from Shape
# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__()
#         self.set_dimension1(radius)  # Using setter for radius (single dimension)

#     # Polymorphism: Overriding the area method
#     def area(self):
#         return 3.14 * (self.get_dimension1() ** 2)

#     # Polymorphism: Overriding the perimeter method
#     def perimeter(self):
#         return 2 * 3.14 * self.get_dimension1()

# # Main execution
# if __name__ == "__main__":
#     # Rectangle object
#     rectangle = Rectangle(10, 5)
#     print(f"Rectangle Area: {rectangle.area()}")  # Polymorphism in action
#     print(f"Rectangle Perimeter: {rectangle.perimeter()}")  # Polymorphism in action

#     # Circle object
#     circle = Circle(7)
#     print(f"Circle Area: {circle.area()}")  # Polymorphism in action
#     print(f"Circle Perimeter: {circle.perimeter()}")  # Polymorphism in action

# # Abstraction

# # In Python, ABC, abc, and abstractmethod are related to the concept of Abstract Base Classes (ABCs), which allow you to define abstract classes that cannot be instantiated directly but can be used as templates for other classes. This is a fundamental concept in Object-Oriented Programming (OOP) to create a common interface that must be implemented by any derived classes.

# # Breakdown:
# # ABC (Abstract Base Class):

# # ABC is a class provided by the abc module in Python.
# # It serves as a base class for defining abstract classes.
# # An abstract class is a class that cannot be instantiated on its own and is intended to be subclassed by other classes that implement its abstract methods.
# # abc (Module):

# # abc is a module in Python that stands for "Abstract Base Class".
# # It provides tools to define abstract classes and abstract methods.
# # You can use this module to create your own base classes that enforce certain methods to be implemented by subclasses.
# # abstractmethod (Decorator):

# # abstractmethod is a decorator provided by the abc module.
# # It is used to mark methods in an abstract class as abstract.
# # An abstract method is a method that is declared but does not have any implementation in the abstract class.
# # Subclasses are required to override and provide an implementation for these methods.



# Polymorphism in Object-Oriented Programming (OOP) refers to the ability of objects of different classes 
# to be treated as objects of a common superclass. It allows the same method to behave differently based 
# on the object that is calling it. There are two types of polymorphism:

# Compile-time Polymorphism (Method Overloading): Occurs when multiple methods have the same name but differ 
# in the number or type of parameters.
# Run-time Polymorphism (Method Overriding): Occurs when a subclass provides a specific implementation of a
#  method that is already defined in its superclass.

# Example of Polymorphism (Method Overriding):

# class Animal:
#     def sound(self):
#         print("This animal makes a sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# # Polymorphism in action
# def make_sound(animal):
#     animal.sound()

# # Creating instances of Dog and Cat
# dog = Dog()
# cat = Cat()
# an=Animal()


# make_sound(dog)  
# make_sound(cat)
# make_sound(an) 