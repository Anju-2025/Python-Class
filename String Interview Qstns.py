# x="The World of Python"
# print(x)
# print(x[4])
# print(x[2:8])
# print(x[2:])
# print(x[:8])
# print(x[-1])
# print(x[-2:])
# print(x[:-5])

y=28
# z="I am Anjali, I am"
# print(z.format() ,y)
# print(z.split())
# print(z.split(','))
# print(z.upper())
# print(z.lower())
# print(z.capitalize())
# print(z.casefold())

# x="5"
# print(int(x))
# how to convert a string into a list? It can be done using split
# x="They are lovely animals"
# print(x.split())

#                                                  Reverse a string by three ways
# (1)  Using a  for loop 


# input_string=input("enter the string: ")
# reverse_string=" "
# for i in input_string:
#     reverse_string=i + reverse_string
# print(reverse_string)

# (2)Using slicing

                        # a="hello darling"
                        # rev=a[::-1]
                        # print(rev)

# (3)Using ".join(reversed())" within a function


                        # def reverse(str):
                        #     rev_str=''.join(reversed(str))
                        #     return rev_str

                        # s="hello"
                        # r=reverse(s)
                        # print("originalstring: ",s)
                        # print("reversed string: ",r)
# def reverse_a_string(string):
#     rev_str=''.join(reversed(string))
#     return rev_str

# x=input("enter a string:")
# r=reverse_a_string(x)
# print(x, "original string")
# print(r, "reversed string")

# (4) convert a string to list and then using length of String using while loop 
# and join, reverse it and again convert to string

                        # s = "Python" # initial string
                        # reversedString=[]
                        # index = len(s) # calculate length of string and save in index
                        # while index > 0: 
                        #     reversedString += s[ index - 1 ] # save the value of str[index-1] in reverseString
                        #     index = index - 1 # decrement index
                        # print(reversedString) 


                        # s="hello"
                        # l=len(s)
                        # list=[]
                        # while l>0:
                        #     list+=s[l-1]
                        #     l=l-1
                        #     string=''.join(list)
                        # print(string)

# W3RESOURCES - 113 EXERCISES + SOLUTION

# 1) Write a Python program to calculate the length of a string.

# a="hello"
# l=len(a)
# print(l)

# def string_length(x):
#     count=0
#     for i in x:
#         count+=1
#     return count

# x=str(input("enter the string: "))
# print(string_length(x))

# 2) Write a Python program to count the number of characters (character frequency) in a string.

def solve(string):
    output={}
    for i in string:
        keys=output.keys()
        if i not in keys:
            output[i]=1
        else:
            output[i]+=1
    return output
print(solve("javaa"))




# a="good vibes good life"
# b=list(a)
# # print(b)
# freq=[b.count(x) for x in b]
# d=dict(zip(b,freq))
# print(d)


# str=str(input("enter a string: "))
# for i in str:
#     print(i,"=",str.count[i])

# list comprehension

# a=["apple","orange","grapes","guava"]
# # b=[x if x !="guava" else "pineapple" for x in a]
# # print(b)


# c=[x for x in a if "a" not in x]
# d=[x for x in a if "a" in x]
# print(c)
# print(d)

# x=[x for x in range(11)]
# print(x)
# a=[x for x in range(10) if x<6]
# print(a)
# print(len(a))

# a=["apple","Orange","grapes","Guava"]
# b=[x.upper() for x in a]
# print(b)
# c=[x.capitalize() for x in a]
# print(c)
# d=[x.lower() for x in a]
# print(d)


# How to swap two numbers using temporary variable

# num1=10
# num2=20
# print("value of num1 before swap:",num1)
# print("value of num2 before swap:",num2)
# temp=num1
# num1=num2
# num2=temp
# print("value of num1 after swap:",num1)
# print("value of num2 after swap:",num2)

#  How to swap two numbers without usig temporary variable


# num1=input("enter the number:")
# num2=input("enter the number:")
# print("value of num1 before swap:",num1)
# print("value of num2 before swap:",num2)
# num1,num2 = num2,num1
# print("value of num1 after swap:",num1)
# print("value of num2 after swap:",num2)

# Check a number is prime or not


# num=int(input("enter the number:"))
# if num<2:
#     print(num,"is not a prime number")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print(num,"is not  a prime number")
#             break
#     else:
#         print(num,"is  a prime number")


# Find factorial of a number
        
# num=int(input("enter the number:"))
# factorial=1
# if num<0:
#     print("factorial does not exist")
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial*=i
#     print(factorial)


# Fibbnocci series



# LIST PRACTICE QUESTIONS
    
# SUM OF NUMBERS IN A LIST

# def sum_list(items):
#     sum_numbers=0
#     for x in items:
#         sum_numbers+=x
#     return sum_numbers
# print(sum_list([1,2,3,4,5]))

# a=[1,2,3,4,5]
# sum=0
# for i in a:
#     sum+=i
#     i+=1
# print(sum)

# a=[1,2,3,4,5]
# sum=0
# for i in range(0,len(a)):
#     sum+=a[i]
# print(sum)


# a=[1,2,3,4,5]
# sum=0
# i=0
# while i <len(a):
#     sum+=a[i]
#     i+=1
# print(sum)


# MULTIPLY ALL ITEMS IN A LIST

# a=[1,2,3,4,5]
# factorial=1
# for i in a:
#     factorial*=i
# print(factorial)

# GET LARGEST NUMBER FROM A LIST

# a=[1,2,3,4,0,-1]
# max=a[0]
# # print(max)
# for i in a:
#     if i>max:
#         max=i
# print(max)


# GET SMALLEST NUMBER FROM A LIST

# a=[-1,2,3,4,0,12]
# min=a[0]
# for i in a:
#     if i<min:
#         min=i
# print(min)

# a=['anjali','arya','week','day']
# print(len(a))
# # print(len(a[0]))
# NUMBER OF CHARACTERS IN A STRING
# string='anjali'
# count=0
# for i in string:
#     count+=1
# print(count)

# def match_word(list):
#     count=0
#     for i in list:
#         if len(i)>1 and i[0]==i[-1]:
#             count+=1
#     return count
# print(match_word(['anjali','arya','surya','veera']))


# def last(n):
#     return n[-1]

# def sort_list_last_element(tuple):
#     return sorted(tuple,key=last)

# print(sort_list_last_element([(1,2),(4,1),(3,3),(8,4)]))

# list=[(2,3),(1,7),(3,6),(1,0)]

# def last_element(tuple):
#     return tuple[-1]

# list1=sorted(list,key=last_element)

# print(list1)

# list=[(2,3),(1,7),(3,6),(1,0)]
# def last_number(tuple):
#     return tuple[-1]
# list1=sorted(list,key=last_number)
# print(list1)


# HOW TO REMOVE DUPLICATE ENTRIES


# list=[10,20,30,20,10,40,50,30]

# def remove_duplicate(my_list):
#     no_dup_list=[]
#     for element in my_list:
#         if element not in no_dup_list:
#             no_dup_list.append(element)
#     return no_dup_list
# print(remove_duplicate(list))

# CHECK A LIST IS EMPTY OR NOT

# list=[]
# def check_empty(my_list):
#     if not my_list:
#         print("list is empty")
#     else:
#         print("list is not empty",my_list)

# check_empty(list)

# l=[]
# list="The last days at college was memorable"
# list2=list.split(" ")

# for i in list2:
#     if len(i)>3:
#         l.append(i)
# print(l)
    
# list1=[1,2,3,4,5]
# list2=[5,6,7,8,9]

# for x in list1:
#     for y in list2:
#         if x==y:
#             result=True

# print(result)
# print("common element is",x)

# a=['ammu','anu','soorya','yamuna','ganga','kaveri','geethu','mintu','pinky','shalu']
# odd_list=[x for (i,x) in enumerate(a) if i not in (0,2,4,6, 8, 10) ]
# even_list=[x for (i,x) in enumerate(a) if i not in(1,3,5,7,9) ]

# print("odd list: ",odd_list)
# print("even_list: ",even_list)

# 



# x=[10,8,1,2,3,4,5]
# x.sort()
# y=set(x)
# y.remove(max(y))
# print(y)
# print("second largest number: ",max(y))

# x=[10,8,1,2,3,4,5]
# x.sort()
# print(x[-2])


# x=[1,2,3,4,1,3,6,4]
# def remove_duplicates(list):
#     no_dup_list=[]
#     for i in list:
#         if i not in no_dup_list:
#             no_dup_list.append(i)
#     return no_dup_list
# print(remove_duplicates(x))

# x=[1,2,3,2,4,5,5,6]
# print("original list: ",x)
# print(list(set(x)))

# list comprehension

# x=[1,2,3,2,4,4,7]
# list=[]
# [list.append(i) for i in x if i not in list]
# print(list)

# enumerate function

# remove even numbers from list

# x=[1,2,3,4,5,6,7,8,9,10]
# even_numbers=[i for i in x if i % 2==0]
# print(even_numbers)

# k=[0,1,2,3,4,5,6,7,8,9,10]
# non_prime_numbers=[]
# for i in k:
#     if i==0 or i==1:
#         continue
#     for j in range(2,i//2+1):
#         if i%j==0:
#             break
#         else:
#             non_prime_numbers.append(i)




# x="python"
# print(x[-1])
# print(x[-5:-1])
# print(x[-5:])
# print(x[:-2])]
x="edugames"
# print(x[3:7])
# print(x[-5:-1])

# print(x[1:4])
# print(x[-7:-4])

# print(x[-4])
# print(x[4])

# print(x[-5:-3])
# print(x[3:5])

# print(x[1:3])
# print(x[-7:-5])

# print(x[5])
# print(x[-3])
# x="classmate"
# print(x[5:])
# print(x[-4:])
# print(x[:5])
# print(x[-9:-4])

# print(x[3:5])
# print(x[-6:-4])

# print(x[-4:])
# print(x[5:])

# Iterators and Generators  here, "it " is the iterator.

# nums=[1,2,3,4]
# it=iter(nums)
# print(it.__next__())

# print(next(it))

# creating new iterator
# class TopTen:
#     def __init__(self):
#         self.num=1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.num<=10:
#             val=self.num
#             self.num+=1
#             return val
#         else:
#             raise StopIteration
# values=TopTen()

# print(next(values))
# print(next(values))
# print(values.__next__())

# for i in values:
#     print(i)


# Generator no need to create class, only function is enough, use yield keyword, as it is not return, its not stopping

# def topten():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# values = topten()
# print(values.__next__())



# def topten():
#      n=1
#      while n<=10:
#           sq=n*n
#           yield sq
#           n+=1
# values=topten()

# for i in values:
#      print(i)
     
        










#