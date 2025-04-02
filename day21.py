
# def function_name(p, q):
#     print(p+q)

# # function_name(10, 20)
# # function_name('hai','hello')
# function_name(10,"hai")
# # 10 ---argument
# p--parameter


# def show(k):
#     for i in k:
#         if (i%5==0):
#             print(i)

# d=[10,21,30,40]
# show(d)

# def display(a, b=90):
#     print(a, b)
# display(10,20)
# display(80)












# arbitrary argument - more than one arguments in single parameter. here, arugemnts appear in tuple format
# def show(*a):
#     print(a)
# show(1,2,3)

# def display(*a):
#     print("hello",a)
# display(1,2,3,4)

# x=100
# def sum(z):
#     print(z)
#     z=50
#     print(z)
# sum(x)

# print(x)

# arbitary arguments(*args)
# def show(*a):
#     print(a)
# show(1,2,3,4)

# # keyword arguments (kwargs)
# def display(b,a,c):
#     print(a,c,b)
# display(a=10,b=20,c=30)

# # # # arbitary keyword arguments (**kwargs)
# def show(**k):
#     print(k)
# show(a=10,b=20,c=30)
    

# a---global variable ---declare outside functions
# a=10
# def show():
#     print(a)
# show()

# a--local variable --declared inside a function
# def show():
#     a=10
#     print(a)
# show()

# print(a)

# def show():
#     global a
#     a=10
#     print(a)
# show()

# print(a)


# scope of a variable ---local,global






# def show(v):
#     print(v)
# show([10,20,30])



# x=100
# def show():
#     global n     if global is given, the variable n is valuable only inside the function.
#     n=50
#     print(n)
# show()
# print(x)

#  pass by value    Do not affect original value outside the function
                #    Here copy of value is passed to function- thus doesnt change outside the function
                    #  choose immutable values - such as integers

# def show(z):
#     print(z)
#     z=50
#     print(z)
# x=20
# show(x)
# print(x)

# pass by reference       affects original value inside and outside the function 
                    # here original value is passed to the function
                    # choose mutable values such as list

# def display(k):
#     k[0]=100
#     print(k)
# l=[1,2,3,4]
# display(l)
# print(l)


# a=10
# a--global variable

# def show():
#     print(a)
# show()



# s--local
# def play():
#     global s
#     s=20
#     print(s)

# play()

# print(s)



# def show(a, b):

#     print(a**2)
#     return b**2

# print(show(20, 30))








# # Recursion - function calling function itself

# def show(a):
#     return a
# print(show(10))



# def show(n):
#     if n<=0:
#         return n
    
#     else:
#         return n + show(n-1)       

# print(show(5))


# def show(n):
#         if (n<=1):
#              return 1
#         else:
#             return n * show(n - 1)
# print(show(5))  


# def show(n):
#     result = 1  
    
#     while n > 1:
#         result *= n  
#         n -= 1  
    
#     return result

# print(show(5))


# # #Factorial of a number

# def show(n):
#     if n<=1:
#         return n
#     else:
#         return n * show(n-1)
    
# print(show(5))

# Fibbonoci series 0,1, 1, 2, 3, 5, 8, 13, 21

# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return (fib(n-1)+ fib(n-2))
# n=int(input("enter the limit:"))
# for i in range(n):
#     print(fib(i))

# def fib(i):
#     if i==0:
#         return 0
#     elif i==1:
#         return 1
#     else:
#         return fib(i-1) + fib(i-2)
# print(fib(10))

# def fib(i):
#     if i==0:
#         return 0
#     elif i==1:
#         return 1
#     else:
#         return fib(i-1) + fib(i-2)

# for x in range(8):
#     print(fib(x))

# simple:
# def fib(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     else:
#         print(a)
#         print(b)

#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
# x=int(input("enter a number: "))
# fib(x)

# k=[]

# for i in range(1, 11):
#     if (i%2==0):
#         k.appned(i)
# print(k)

# print([ i**2 for i in range(1, 11) if i%2!=0])


# lambda syntax:
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
# from functools import reduce
# a=[1,2,3,4,5,6,7,8,9,10]
# x=reduce(lambda z,y:z+y,a)
# print(x)

#  #write a program to find the numbers greater than zero from the list below. 

# a=[18,3,5,0,-1,12]
# x=list(filter(lambda z:z>0,a))
# print(x)




A=["","one","two","three","four","five","six","seven","eight","nine","ten"]
C=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","ninteen"]
B=[" "," ","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty","hundred"]
n=int(input("enter a number:"))
if n<=10:
    print(A[n])
elif n>10 and n<20:
    y=n%10
    print(C[y])
elif n>=20 and n<=100:
    ones=n%10
    tens=n//10
    if ones==0:
        print(B[tens])
    else:
        print(B[tens] + A[ones])


# try:
#     # Code that might raise an exception
# except SomeException as e:
#     # Code that runs if the exception occurs
# else:
#     # Code that runs if no exception occurs
# finally:
#     # Code that runs no matter what (whether an exception occurs or not)
