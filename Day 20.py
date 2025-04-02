#python program to count and display words in a text file.


# f=open("anu.txt","r")
# p=f.readlines()
# count=0
# for i in p:
#     count=count+1
# print("number of words in file is",count)
# print(p)
# f.close()


# f=open('word.txt','r')
# a=f.read()
# p=a.split()
# k=len(p)
# print(p)
# print(k)
# f.close()

# f=open('hai.txt',"r")
# a=f.read()
# p=a.split()
# u=[]
# for i in p:
#     k=int(i)
#     u.append(k)
# print(u)
# print(max(u))
# print(min(u))
# f.close()

# import os
# os.remove("file name")   # to delete file
# os.rmdir("folder name")  # to delete empty folder
# import shutil
# shutil.rmtree("folder name") # to delete folder with some files or content





# def function_name(a): a- parameter
#     block of codes
# function name(10)  10 - argument

# print(sum([

# def show(a, b):
#     print(a+b)

# show(10, 20)
# 10---argument
# a----parameter





# def show(a,b,c):
#     print("welcome",a+b*c)
# show(10,20,5)


# def show(a,b=18):
#     print("welcome",a,b)
# show("ammu",10)
# show("anu")
# show("devu","ramu")

# def sum(a,b):
#     print("sum =",a+b)
# sum(100, 20)

# def diff(a,b):
#     print("diff",a-b)
# diff(100, 80)


# def show(a,b):
#     print(a*b)
# show(10,5)


# 

                                            # How to pass a list in a function
# def display(x):
#     print(x)

# display([1,3,4])

# def show(a):
#     print(a**2)
# show(5)



# def show(a):
#     return a

# print(show(10))

# def show(u):
#     print(u)
# x=[20,30,40]
# show(x)



# def display(x):
#     for i in x:
#         print(i)
# p=[1,2,3,4,5]
# display(p)

                            # return
# def show(a,b):
#     return a+b
    
  
# print(show(10,10))


# def show(a,b):
#     return a*b
# p=show(10,5)
# print(p)


# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# print("select operation:")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Division")
# print("5.Exit")
# while True:
#     choice =input("Enter a choice(1/2/3/4/5):")
#     if choice =='5':
#         print("Exiting calculator")
#         break
#     if choice in ('1/2/3/4'):
#         num1 = float(input("Enter first number:"))
#         num2 = float (input("Enter second number:"))
#         if choice =='1':
#             print(num1,'+', num2,'=',add(num1,num2))
#         elif choice =='2':
#             print(num1,'-',num2,'=',sub(num1,num2))
#         elif choice=='3':
#             print(num1,'*',num2,'=',mul(num1,num2))
#         elif choice =='4':
#             if num1>num2:
#                 print(num1,'/',num2,'=',div(num1,num2))
#             else:
#                 print("invalid division")
#     else:
#         print("invalid choice, pls try again.")



#python program to convert number into words using list
# A = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
# C = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
# B = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# n = int(input("enter a number: "))

# if n <= 10:
#     print(A[n])
# elif n == 20:  # Special case for exactly 20
#     print("twenty")
# elif 10 < n < 20:
#     y = n % 10
#     print(C[y])
# elif 20 < n < 100:
#     ones = n % 10
#     tens = n // 10
#     if ones == 0:
#         print(B[tens])
#     else:
#         print(B[tens] + " " + A[ones])
# elif n == 100:  # Special case for exactly 100
#     print("hundred")


# A = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven"
#      ,12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen"
#      ,16:"sixteen",17:"seventeen",18:"eighteen",19:"ninteen"
#      ,20:"twenty",30:"thirty",40:"forty",50:"fifty"
#      ,60:"sixty",70:"seventy",80:"eighty",90:"ninty",100:"hundred"}
# n=int(input("enter a number:"))
# if n<=100:
#     if n in A:
#         print(A.get(n))
#     else:
#         r=n%10
#         q=n//10
#         q=q*10
#         print(A.get(q),A.get(r))
# else:
#     print(n,"enter a number<=100")


# def show(a,b):
#     pass
# show(10, 20)





# arbitrary argument (*args)
# def show(*k):
#     print(k)

# show('hello',10, 20, 30)


# keyword argument(kwargs)
# def show(c, b, a):
#     print(a)
#     print(b)
#     print(c)

# show(a=10, b=20, c=30)

# arbitrary keyword argument(**kwargs)
# def show(**f):
#     print(f)
   

# show(a=10, b=20, c=30)


# scope of a variable --global, local
# global variable
# a=10
# print(a)
# def show(k):
#     k=40
#     print(k)
# show(k=a)

# print(a)

# a--local variable (defined inside a function)
# def show():
#     a=20
#     print(a)
# show()
# print(a)

# print(a)

# def show():
#     global a
#     a=30
#     print(a)
# show()
# a=12
# print(a)


# def show(n):
#     for i in n:
#         if (i%5==0):
#             h.append(i)
#     print(h)


# h=[]
# f=[10, 20, 30, 31, 21, 81]
# show(f)
# show([20, 30, 40, 60])



# def show(a, b):
#     print(a-b)
#     return a+b
# show(20,10)
# print(show(10, 20))



# d='aeiouAEIOU'
# l=[]
# count=0
# st=input("enter a string:")

# for i in st:
#     if (i in d):
#         l.append(i)
#         count+=1
#     else:
#         print(st,"doesnt have any vowels, it is a complete consonent word")
# print(l,"are the vowels in",st)
# print(count,"is the count of vowels in ",st)


# print('hello'*2)
# for loop and while loop

# for item in iterabe
# iterable ---list, tuple, string, range


# for i in range(1,11):
#     print('hello')

# for i in range(1, 11):
#     # print(i)
#     print(i,end=' ')


# d="hello"
# for i in d:
#     print(i)


# d='hello dear python'
# for i in d.split():
#     print(i)



# f=[10,20,30]
# for i in f:
#     print(i)

# sum=0
# f=[10,20,30]
# for i in f:
#     sum+=i

# print(sum,"is the sum of numbers in the given list")



# g=("hello", 10, True)

# for i in g:
#     print(i)

#     lambda syntax:
# lambda parameters:expression

# def show(a, b):
#     print(a+b)
# show(4,5)

# x=lambda a,b:a+b
# print(x(4,5))

# x=lambda a,b:a*b
# print(x(10,3))

# x=lambda a,b:a%b
# print(x(20,6))

# x=lambda a,b: a +" "+"welcome"+" "+b
# print(x("ammu","anu"))


# lambda- filter, map, reduce
# filter: This function is used to filter elements of a sequence based on a condition. 

# a=[1,2,3,4,5,6,7,8,9,10]
# x=list(filter(lambda x:x%2==0,a))     
# print(x)



# map: This function applies a specified function to all elements in an iterable (like a list). 
# a=[1,2,3,4,5,6,7,8,9,10]
# x=list(map(lambda z:z**3,a))
# print(x)

# reduce: This function applies a rolling computation to the elements of a 
# sequence (cumulatively applying the function from left to right). 
from functools import reduce
a=[1,2,3,4,5,6,7,8,9,10]
x=reduce(lambda z,y:z+y,a)
print(x)

 #write a program to find the numbers greater than zero from the list below. 

# a=[18,3,5,0,-1,12]
# x=list(filter(lambda z:z>0,a))
# print(x)



