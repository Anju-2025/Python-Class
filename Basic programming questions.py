# Variable Declaration


            #  1) Write a program to declare integer, character, float, boolean, and display it

#a=10
# print(a)
# print(type(a))

# string = "Anjali"
# print(string)
# print(type(string))

# a=5.5
# print(a)
# print(type(a))

# a=True
# print(a)
# print(type(a))

                    # 2) Write a program to print 'Hello world'
# print("Hello world")

                    # 3) write a program to find sum of two numbers and display it
# a=10
# b=20
# sum=a+b
# print("sum is",sum)

#        OR
# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# print("sum of two numbers is",a+b)

                    # 4) write a program to find and display difference between two numbers

# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# diff=a-b
# print("Difference is",diff)

                        # 5) write a program to find cube of a number

# a=int(input("enter a number: "))
# cube=a**3
# print("cube is",cube)

                            # 6) write a program to swap two numbers
# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# print("value of first number before swapping: ",a)
# print("value of second number before swapping: ",b)
# k=a
# a=b
# b=k
# print("value of first number after swapping: ",a)
# print("value of second number after swapping: ",b)
                            # 7) write a program to find factorial of a number

# a=int(input("enter a number: "))
# factorial=1
# if a<0:
#     print("factorial does not exist for numbers less than zero")
# elif a==0:
#     print("factorial of zero is 1")
# else:
#     for i in range(1,a+1):
#         factorial*=i
#     print("factorial is",factorial)


# 5=5 x 4 3 x 2 1
# num=int(input("enter a number: "))
# factorial=1
# if num<0:
#     print("factorial can be counted for numbers greater than 1 only")
# elif num==0:
#     print("factorial of zero is 1")
# else:
#     for i in range(1, num+1):
#         factorial*=i
# print(factorial)

# sum=0
# num=int(input("enter a number: "))
# for i in range(1, num+1):
#     sum+=i
# print(sum)

2, 3, 5, 7, 11, 13, 17, 19, 

# prime number-----2, 3, 5, 7, 11, 13, 17, 19, 23, 29, --------


# num=int(input("enter a number: "))
# if num<=1:
#     print(num, "is not in prime number range")
# elif num>1:
#     for i in range(2, num):
#         if (num%i==0):
#             break
#     else:
#         print(num,"is a perfect prime number")





                                # if statement

                                # 8) find the largest of two numbers

# n1=int(input("enter a number: "))
# n2=int(input("enter a number: "))
# if n1>n2:
#     print(n1,"is the largest")
# else:
#     print(n2,"is the largest")

                                    # 9) find the largest of three numbers

# n1=int(input("enter first number: "))
# n2=int(input("enter second number: "))
# n3=int(input("enter third number: "))
# if n1>n2 and n1>n3:
#     print(n1,"is the largest number")
# elif n2>n1 and n2>n3:
#     print(n2,"is the largest number")
# else:
#     print(n3,"is the largest number")

                                        # 10) find given number is even or not
# n=int(input("enter a number: "))
# if  n%2==0:
#     print(n,"is an even number")
# else:
#     print(n,"is not an even number")

                                        # 11) find given number is odd or not
# n=int(input("enter a number: "))
# if n%2!=0:
#     print(n,"is an odd number")
# else:
#     print(n,"is not an odd number")

                                    # 12) check the given number is divisible by 2 and 5
# n=int(input("enter a number: "))
# if n%2==0 and n%5==0:
#     print(n,"is divisible by 2 and 5")
# elif n%2==0 and n%5!=0:
#     print(n,"is divisible by 2 but not divisible by 5")
# elif n%5==0 and n%2!=0:
#     print(n,"is divisible by 5 but not divisible by 2")
# else:
#     print(n,"is not divisible by 2 and 5")
                            # 13) Check the given number is amstrong or not

# n=int(input("enter a number: "))
# num1=n
# num2=n
# count=len(str(n))
# sum=0

# while num1>0:
#     e=num1%10
#     sum+=e**count
#     num1//=10
# print(sum)

# if sum==num2:
#     print(num2,"is armstrong")
# else:
#     print(num2,"is not armstrong")

# num=int(input("enter a number: "))
# num1=num
# num2=num
# sum=0
# count=len(str(num))
# while num1>0:
#     e=num1%10
#     sum+=e**count
#     num1//=10
# if num2==sum:
#     print(num2,"is amstrong")
# else:
#     print(num2,"is not amstrong")


# n=int(input("enter a number:"))
# reverse=0
# num1=n
# while n>0:
#     x=n%10
#     reverse=reverse*10 + x
#     n//=10
# if reverse==num1:
#     print(num1,"is palindrome")
# else:
#     print(num1,"is not palindrome")





# num=int(input("enter a number: "))
# x=num
# y=num
# count=0
# arm=0

# while num>0:
#     count+=1
#     num//=10
# print(count)

# while x>0:
#     e=x%10
#     arm=arm + e**count
#     x//=10
# print(arm)

# if arm==y:
#     print(y,"is armstrong")
# else:
#     print(y,"is not armstrong")

                        # LOOPS

   



# # 15) check a number is prime or not

# num=int(input("enter a number: "))
# for i in range(2,num):
#     if num%i==0:
#         print(num,"is not a prime number")
#         break
# else:
#     print(num, "is a prime number")

# n=int(input("enter a number: "))
# for i in range(2,n):
#     if n%2==0:
#         print(n,"is not prime")
#         break
# else:
#     print(n,"is a prime number")


# n=int(input("enter a number: "))
# count=0
# for i in range(2,n+1):
#     if n==2:
#         print(n,"is the smallest prime number")
#     elif n<2:
#         print("invalid number")
#     else:
#         if n%i==0:
#             count+=1
#     if count==2:
#         print(n,"is a prime number")
#     else:
#         print(n,"is not a prime number")
    

    
# STAR PATTERN PROGRAMS
    
# rows=5
# n=1
# for num in range(rows):
#     for col in range(num+1):
#         print(n,end=' ')
#     n+=1
#     print()
    
# rows=5
# n=5
# for num in range(rows):
#     for col in range(num+1):
#         print(n,end=" ")
#     n-=1
#     print()

# rows=5
# for num in range(rows):
#     n=1
#     for col in range(num+1):
#         print(n,end=" ")
#         n+=1
#     print()

# rows=5
# for num in range(rows):
#     n=5
#     for col in range(num+1):
#         print(n,end=" ")
#         n-=1
#     print()








# print('"I love my country"')
# print("I am \\n Anjali")
# print(10.0//3)
# x=2E3
# print(type(2E3))

# for i in 765<1:
#     print(i)

# print(ord('A'))
# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))



# x="python" 
# y="Python"
# print(x==y)    Order number of 'p' > Order number of 'P'
# print(x>=y)

# str1="hello"
# str2="my world of love"
# print(str1[0])
# print(str2[3:8])
# print(str1[::-1])
# print(len(str2))

# x=input("enter  a string: ")
# rev_x = x[::-1]
# if rev_x==x:
#     print("the string is pallindrome")
# else:
#     print("the string is not palindrome")

# x=input("enter a string: ")
# count=0
# for i in x:
#     count+=1
# print("length of string is: ", count)


# PROGRAMS - PRACTICE QSTNS

# def char_frequency(str):
#     dict={}
#     for n in str:
#         keys=dict.keys()
#         if n in keys:
#             dict[n]+=1
#         else:
#             dict[n]=1
#     return dict
# print(char_frequency('madam'))


# def string_both_ends(str):
#     if len(str)<2:
#         return ''
#     else:
#         return str[0:2] + str[-2:]
# # print(string_both_ends('w'))
# # print(string_both_ends('wx'))
# print(string_both_ends('anjali'))

# def change_char(str1):
#     char=str1[0]
#     str1=str1.replace(char,'$')
#     str1=char+str1[1:]
#     return str1
# print(change_char("anjali"))

# def string_mix(a,b):
#     new_a=b[:2]+a[2:]
#     new_b = a[:2]+b[2:]
#     return new_a + '' + new_b
# print(string_mix('abc','xyz'))


# def change_string(str):
#     if len(str)>2:
#         if str[-3:]=="ing":
#             str+='ly'
#         else:
#             str+='ing'
#     return str
# print(change_string('ab'))
# print(change_string('walk'))
# print(change_string('string'))


# for i in range(1, 11):
#     if (i%2==0):
#         print(i)





# LIST COMPREHENSION
# List comprehension is a concise way to create lists by writing the expression followed by a for loop, 
# and optional conditionals, all in one line. 
# It’s a more compact and readable way to generate lists compared to traditional for loops.
# SYNTAX
# [expression for item in iterable if condition]

# expression: The expression or operation you want to perform on each item.
# item: Variable that represents each element from the iterable.
# iterable: Any iterable object (like a list, range, etc.).
# condition: (Optional) A condition to filter elements.


# squares = [x**2 for x in range(5)]
# print(squares)  # Output: [0, 1, 4, 9, 16]

# x=[]
# for i in range(1, 10):
#     if (i%2==0):
#         x.append(i)
# print(x)




# even_squares = [x**2 for x in range(10) if x % 2 == 0]
# print(even_squares)  


# Given two lists keys and values, 
# use dictionary comprehension to generate a dictionary where keys are mapped to values.


# keys = ['a', 'b', 'c']
# values = [1, 2, 3]

# dictionary = {keys[i]: values[i] for i in range(len(keys))}

# print(dictionary)

# Given a sentence, use list comprehension to create a list of the first letter of each word.


# sentence = "List comprehension is powerful"
# first_letters = [word[0] for word in sentence.split()]

# print(first_letters)

# Create a list comprehension to generate all pairs of numbers (x, y) where x is from 1 to 3 and y is from 1 to 2.


# pairs = [(x, y) for x in range(1, 4) for y in range(1, 3)]

# print(pairs)

# Write a list comprehension to find all palindromes in a given list of strings.

# 		Input: ["madam", "racecar", "apple", "level", "world"]



# words = ["madam", "racecar", "apple", "level", "world"]
# palindromes = [word for word in words if word == word[::-1]]

# print(palindromes)




# p = [x for x in range(2, 50) if all(x % i != 0 for i in range(2, x))]

# print(p)


# Given a string, use list comprehension to create a new string with all the vowels removed.

# 	Input: "beautiful day"


# input_string = "beautiful day"
# vowels = "aeiouAEIOU"
# result_string = ''.join([char for char in input_string if char not in vowels])

# print(result_string)




# keys = ['a', 'b', 'c']
# values = [1, 2, 3]

# dictionary = {}

# for i in range(len(keys)):
#     dictionary[keys[i]] = values[i]

# print(dictionary)

# dictionary = {keys[i]: values[i] for i in range(len(keys))}

# print(dictionary)


# sentence = "List comprehension in Python"
# first_letters = [word[0] for word in sentence.split()]

# print(first_letters)


# class A:
#     def __init__(self, a):
#         self.a = a
#         print(self.a)

#     def __add__(self, other):
#         return self.a + other.a


# a1 = A(10)  
# a2 = A(20)  


# result = a1 + a2  
# print(result) 

# Fibonacci series using for loop

# 0 1 1 2 3 5 8

# n = int(input("enter a number: "))  
# a, b = 0, 1

# print("Fibonacci series using for loop:")
# for i in range(n):
#     print(a, end=" ")
#     a=b
#     b=a+b


# # Fibonacci series using while loop
# n = 10  
# a, b = 0, 1
# count = 0

# # print("\nFibonacci series using while loop:")
# while count < n:
#     print(a, end=" ")
#     a, b = b, a + b
#     count += 1


# # try:
# #     # Code that might raise an exception
# # except SomeException as e:
# #     # Code that runs if the exception occurs
# # else:
# #     # Code that runs if no exception occurs
# # finally:
# #     # Code that runs no matter what (whether an exception occurs or not)


# # d={}
# # d["name"]=["devika"]
# # print(d)

# # # try:
# # #     # Code that might raise an exception
# # except SomeException as e:
# #     # Code that runs if the exception occurs
# # else:
# #     # Code that runs if no exception occurs
# # finally:
# #     # Code that runs no matter what (whether an exception occurs or not)



# # try:
# #     num = int(input("Enter a number: "))
# #     result = 10 / num
# #     print(f"Result: {result}")
# # except ZeroDivisionError as e:
# #     print("Error: You can't divide by zero!")
# # except ValueError as e:
# #     print("Error: Invalid input, please enter a number.")
# # else:
# #     print("The operation was successful.")
# # finally:
# #     print("This will run no matter what.")




# # s="devika python student"
# # # print(s[-1])
# # # print(s[0:4])
# # # print(s[-14:-8])

# # print(s[:])
# # print(s[0:])
# # print(s[:21])

# # print(s[::-1])



# # for loop

# # for i in range(1,11):
# #     print("hello")

# # d=[10,20,30,50,70,100]
# # for i in d:
# #     print(i)

# # d={"name":"devika","age":20}
# # for i in d:
# #     print(i)
# for i in range(1,11):
#     if (i%5==0):
#         print(i**2)

# # iterate a list of numbers using for loop
# # iterate a string using for loop
# # iterate first 10 natural numbers
# # iterate first 20 natural numbers and append all odd numbers in another list
# # iterate first 50 natural numbers and append all multiples of 5 in another list

# class Library:
#     def __init__(self):
#         self.__books = []

#     def add_book(self, book_name):
#         self.__books.append(book_name)
#         print(f'Book "{book_name}" added to the library.')

#     def lend_book(self, book_name):
#         if book_name in self.__books:
#             self.__books.remove(book_name)
#             print(f'Book "{book_name}" lent out.')
#         else:
#             print(f'Sorry, the book "{book_name}" is not available.')

#     def return_book(self, book_name):
#         self.__books.append(book_name)
#         print(f'Book "{book_name}" returned to the library.')

#     def view_books(self):
#         print("Available books:")
#         for book in self.__books:
#             print(f"- {book}")

# library = Library()
# library.add_book("The Great Gatsby")
# library.add_book("1984")
# library.view_books()
# library.lend_book("1984")
# library.view_books()
# library.return_book("1984")
# library.view_books()


# import re

# # Example: Find all words in a string
# def find_words(text):
#     return re.findall(r'\w+', text)

# text = "The quick brown fox jumps over the lazy dog."
# print(find_words(text))
# k=[]
# lower=int(input("enter lower limit number: "))
# upper=int(input("enter upper limit number: "))
# for num in range(lower, upper+1):
#     if num>1:
#         for i in range(2, num):
#             if (num%i==0):
#                 break
#         else:
#             k.append(num)
# print(k)

    

# num=int(input("enter a number"))
# if num<=1:
#     print("not in prime range")
# elif num>1:
#     for i in range(2, num):
#         if (num%i==0):
#             print(num,"is a non prime number")
#             break
#     else:
#         print(num, "is a perfect prime number")


# prime number intervels
# lower_limit=int(input("enter a number"))
# upper_limit=int(input("enter a number"))

# primenumbers=[]

# for num in range(lower_limit,upper_limit+1):
#     if num<=1:
#         print("not in prime range")
#     elif num>1:
#         for i in range(2, num):
#             if (num%i==0):
#                 break
#         else:
#             primenumbers.append(num)
# print(primenumbers)


# get all prime numbers from this list

# f=[1, 100, 2, 80, 7, 6, 5, 37]


# for i in f:
#     if i<1:
#         continue
#     elif i>1:
#         for j in range(2, i):
#             if (i%j==0):
#                 break
#         else:
#             print(i,end=' ')


# check a string is palindrome for not


# d=str(input("enter a string: "))
# if (d==d[::-1]):
#     print(d,"is a proper palindrome string")
# else:
#         print(d,"is not a  palindrome string")


# check a number is palindrome or not

# d=int(input("enter a number: "))
# d=str(d)
# if (d==d[::-1]):
#     print(d,"is a proper palindrome number")
# else:
#         print(d,"is not a  palindrome number")



# get all palindrom words from the sentence given above

# d=" Dear Madam, can we get one racecar and one  level civic radar"
# count=0
# k=[]
# for i in d.split():
#     if (i==i[::-1]):
#         count+=1
#         k.append(i)
# print(k,count)

# check a number is palindrome for not

# num=int(input("enter a number: "))
# org=num
# reverse=0

# while (num>0):
#     digit=num%10
#     reverse= reverse*10 + digit
#     num=num//10
# if (org==reverse):
#     print(org,"is a perfect palindrome number")
# else:
#     print(org,"is not a palindrome number")

# get all palindrome numbers from a list

# list=[1221, 1240, 999, 878, 141]
# pal_list=[]

# for item in list:
#     org=item
#     reverse=0
#     while (item>0):
#         digit=item%10
#         reverse= reverse*10 + digit
#         item=item//10
#     if (org==reverse):
#         pal_list.append(org)
#     else:
#         continue
# print(pal_list)


# check a number is amstrong or not

# num = int(input("Enter a number: "))
# org = num
# sum = 0
# k = len(str(org)) 
# while num > 0:
#     digit = num % 10
#     sum += digit ** k
#     num = num // 10

# if sum == org:
#     print(org, "is an Armstrong number")
# else:
#     print(org, "is not an Armstrong number")



# # num=int(input("enter a number: "))
# # org=num
# # l=len(str(num))
# # sum=0
# # while (num>0):
# #     digit=num%10
# #     sum+=digit**l
# #     num=num//10
# # if (sum==org):
# #     print(org,"is an amstrong number")
# # else:
# #     print(org,"is not an amstrong number")


# # write a python program to check a number is prime or not
# # 2, 3, 5, 7, 11, 13, 17, 19, 23
# # num=int(input("enter a number: "))
# # if num<=1:
# #     print(num, "not in prime number range")
# # else:
# #     for i in range(2, num):
# #         if (num%i==0):
# #             print(num,"is not a prime number")
# #             break
# #     else:
# #         print(num,"is a perfect prime number")

# write a python program to get all prime numbers in a range
k=[]
low=int(input("enter lower limit number: "))
upp=int(input("enter upper limit number: "))
for num in range(low, upp+1):
    if (num>1):
        for i in range(2, num):
            if (num%i==0):
                break
        else:
            k.append(num)
print(k)

# # d=[10,11, 12, 13, 14, 16, 17, 19]

# # write a python program to check a string is palindrome or not

# # level, madam, malayalam

# # string1=input('enter a string: ')
# # if string1==string1[::-1]:
# #     print(string1,"is a palindrome")
# # else:
# #     print(string1,"is not palindrome")


# # write  a python program to check a number is palindrome or not
# # 1221, 2332

# # Num=int(input("enter a number: "))
# # Org=Num
# # reverse=0
# # while(Num>0):
# #     digit=Num%10
# #     reverse=reverse*10 + digit
# #     Num=Num//10
# # if (reverse==Org):
# #     print(Org,"is a palindrome number")
# # else:
# #     print(Org,"is not a plaindrome number")


# word=input('enter a string: ')
# if word==word[::-1]:
#      print(word,'is palindrome')
# else:
#      print(word,'is not palinrome')





# # # write a python program to check a number is amstrong or not

# # d=[10, 2000, -10, -20, 34100, 200]

# # max_num=d[0]
# # min_num=d[0]

# # for i in d:
# #     if (i>max_num):
# #         max_num=i
# #     elif (i<min_num):
# #         min_num=i
# # print(max_num,"is the largest number in the list")
# # print(min_num,"is the minimum number in the list")

# # l=[]

# # s="The World of Python"
# # for i in s:
# #     if (i.isupper()):
# #         l.append(i)
# # print(l)


# s = "The World Of Python and new techs"
# l = []

# for word in s.split():
#     for i in word:
#         if (i.isupper()):
#             l.append(word)

# print(l)

# number=int(input('enter a number: '))
# new=str(number)
# if new==new[::-1]:
#     print(number,'is palindrome')
# else:
#     print(number,'is not palindrome')
