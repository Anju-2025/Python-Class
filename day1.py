# print("hello world!")

# print("python world")
# print("The world of programming langauages")
#print("VS code")

# variable declaration

# a=10
# print(a)
# a_A=20
# A_12 =100
# _12=100



# primary -integer, float, string, boolean



# numeral -integer, float
# a=10
# print(a)
# print(type(a))


# string
# b="   vdffdsf56576!@#=/.,?"
# d="43545657"
# print(type(d))



# float
# c=100.5
# print(c)
# print(type(c))

# boolean
# c=True
# print(type(c))
# simple/primary

# x=10
# print(x)
# x=20
# print(x)
# x=90
# print(x)



# s=input("enter a word: ")
# d=str(input("enter a word: "))
# print(s)
# print(type(s))

# f=int(input("enter a number: "))
# print(f)

# d=float(input("enter your age: "))
# print(type(d))



# a=10
# b=20
# print(a+b,"is the sum of a and b")


# concantenation/joining
# s="hai"
# h="hello"
# print(s+' '+h)

# a="hai"
# b=10
# print(a+b)

# p=input("enter a word: ")
# print(p)
# print(type(p))

# k=int(input("enter a number: "))
# print(k)

# q=input("enter your hobby:")
# print("My hobby is" + " " + q)

# concantenation

# l=(input("enter a number"))   
# print(l)
# print(type(l))

# A=input("enter my name,k") 
# print(A)
# print(type(A))

# b=input("enter a number,k")
# print(b)
# print(type(b))


# a,b,c='apple',"ball","cat"
# print(a,b,c)


# s=10
# s=30
# s=90
# print(s)


# print(A,b)

# c="Dynamic"
# print(c)
# print(type(c))

# print(c,b)

# print(A, b, c)

# a="welcome"
# print(a)
# b="everybody"
# print(b)
# print(a,b)

#Data types - int, string, float, boolean,tuple, list, set, dictionary



# a=10
# b=10
# c=30
# a,b,c=10,20,30
# print(a+b+c)

# a=10
# print(a)
# print(type(a))

# b="wisdom"
# print(b)
# print(type(b))

# c=100.05
# print(c)
# print(type(c))


# d=True
# d=False
# print(d)
# print(type(d))

# tuple
# e=('string',10, 100.5, False, 100, 90, 'hai')
# print(e)
# print(type(e))

# collection datatype
# list --multiple data types, duplicates allow, ordered, mutable
# a=[10,100.78, False,'hai', 10, 10, 10]
# print(a)
# print(type(a))
# print(a)
# a=[]
# a=list()

# print(type(a))
# a=[]
# # print(a[-4])

# # tuple - immutable

# a=(10, 100.4, True, "hai", True)
# d=tuple()
# print(a)
# b=tuple()
# print(b)
# print(type(b))

# set - unordered, no -indexing, no duplicates, mutable, 
# d={10, 100.6, "Hai",False,"Hai"}
# print(d)
# d=set()

# dictionary  - multiple, no duplicates, ordered, mutable
# d={"name":"athul", "age":10, "place":"tvm", "age":20}
# print(d)




# index position ---positive indexing, negative indexing
# d=[10,20,30,40,10,10,10]

# print(len(d))


# g='hello'
# print(g[-2])


# set
# # g={"12th April", 100, False, 0.9}
# # print(g)
# # print(type(g))


# # dictionary
# h={"member":"male","name":"Ammu","age":25, "place":"kochin"}
# print(h)
# print(type(h))


# class Greek:
#     def __init__(self,name,age):
#         self.greekname=name
#         self.greekage=age

#     def displayAge(self):
#         print("Age: ",self.greekage)

# obj=Greek("Anjali",28)
# print("Name: ",obj.greekname)
# obj.displayAge()


# a=[10,20,30]
# print(sum(a))

# indexing and slicing

# d=[10,20,30,40,50,60,70, 80]

# print(d[1],"is the 2nd number in the list")

# print(d[2:5])
# print(d[0:7:2])

# print(d[0:])
# print(d[:8])
# print(d[:])

# print(d[::-1])

# print(d[-4:-2])


# d="hello python"
# print(d[0:5])

# operators

# arithametic operators
# a=20
# b=10
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**3)


# relational
# a=20
# b=10
# a+=b
# # a-=10
# a*=10
# print(a)


# comparison operators >, >=, <. <=.
# a=10
# b=20
# # print(a>b)
# print(a>=b)
# # print(a==b)
# print(a!=b)


# a=10
# a==10


# logical operators --and, or, not
# a=10
# b=20
# c=30
# print(b>a and c<b)
# print(a>b or c>b)
# print(not a>b)

# membership operators in not in
# s="hello"
# print('h' in s)
# print('k' not in s)

# identity operators -is ,is not

# s=90
# n=80
# print(s is n)

# d = [1221, 1441, 1234, 5436, 121]
# reverse = 0
# new = []
# non = []

# for i in d:
#     original = i  
#     reverse = 0 
#     while i > 0:
#         digit = i % 10
#         reverse = reverse * 10 + digit
#         i = i // 10  
    
#     if original == reverse: 
#         new.append(original)
#     else:
#         non.append(original)

# print("Palindrome Numbers:", new)
# print("Non-Palindrome Numbers:", non)


# prime_num=[]
# d=[12, 3, 24, 85, 6, 7, 8, 9, 10, 11, 22, 2, 1, 0, -10]
# for i in d:
#     if i<=1:
#         continue
#     for j in range(2, i):
#         if (i%j==0):
#             break
#     else:
#         prime_num.append(i)

# print(prime_num)


# for loop

# for i in range(10):
#     print('hello',end=' ')


# write a python program to print first 10 natural numbers

# for i in range(1, 11):
#     print(i)

# odd=[]
# even=[]
# for i in range(1, 11):
#     if (i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# sum=0
# for i in range(1, 11):
#     sum+=i
# print(sum,'is the sum of numbers in the given range')

# sq=[]
# cu=[]
# for i in range(1,11):
#     if (i%2==0):
#         sq.append(i**2)
#     else:
#         cu.append(i**3)

# print(sq)
# print(cu)

# count=0
# # for i in range(1,51):
# #     if (i%2==0):
# #         count+=1
# # print(count,'is the count of even numbers in the given range')



# # num=int(input('enter a number: '))
# # str1=str(input('enter a string: '))
# # print(str1)

# # a_A=10
# # _de=10
# # ASS=20
# # a_2=90

# # string
# d='hello dear python'
# print(d.capitalize())
# print(d.title())

# print(d.upper())
# print(d.isupper())
# print(d.isalpha())
# print(d.isdigit())



# h='hello'

# print(len(h))
# # print(h.center(10,'*'))
# # print(h.count('l'))
# # print(h.index('h'))
# print(h.endswith('o'))
# print(h.startswith('k'))
# print(h.find('h'))

# h='hello dear python'
# print(h.split())
# print(h.replace('e','k'))


a=10
a==10

num=int(input('enter a number: '))
if (num%2==0):
    print(num,'is even number')
else:
    print(num,'is an odd number')

