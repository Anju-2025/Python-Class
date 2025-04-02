

# write a python program to check whether a number is prime or not
# prime ---1, num
# examples --2, 3, 5, 7, 11, 13, 17, 19, 23----

# num=int(input("enter a number: "))
# if (num<=1):
#     print(num,"is not in prime number range")
# else:
#     for i in range(2, num):
#         if (num%i==0):
#             print(num,"is not prime")
#             break
#     else:
#         print(num,"is a perfect prime number")


# d=[10,12, 13,14,17, 18, 19]
# prime=[]

# for num in d:
#     if (num<=1):
#         print(num,"is not in prime number range")
#     else:
#         for i in range(2, num):
#             if (num%i==0):
#                 break
#         else:
#             prime.append(num)
# print(prime)



# loops --for loop, while loop
# print('hello'*2)

# for item in iterable
# for i in range(1,11):
#     print('hello',end='*')

# for i in range(10):
#     print('hello')


# get first 20 natural numbers, which are even only
# even=[]
# odd=[]
# for i in range(1,21):
#     if (i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)

# d=[10,11,22, 25, 30,33]
# l1=[]
# l2=[]

# for i in d:
#     if (i%5==0):
#         l1.append(i)
#     else:
#         l2.append(i)
# print(l1)
# print(l2)

# d="python"

# for i in d:
#     print(i)


# g='python programming language'

# for i in g.split():
#     print(i)

# iterable -- range of numbers, list, tuple, string, (set, dictinary)

# k=(10,20,30)
# for i in k:
#     print(i)

# get the factorial of any natural number
# factorial of = 120 (5*4*3*2*1)

# num=int(input("enter a number: "))
# fact=1
# for i in range(1, num+1):
#     fact*=i
# print(fact,"is the factorial of ",num)



# even=[]
# odd=[]
# i=1
# while i<=10:
#     if (i%2==0):
#             even.append(i)
#     else:
#         odd.append(i)
#     i+=1

# print(even)
# print(odd)
# nested loop


# for item in iterable

# for i in range(1,11):
#     if (i%2==0):
#         print(i)

# even=[]
# odd=[]
# i=1
# while(i<=10):
#     if (i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)
#     i+=1

# print(even)
# print(odd)





# i=1
# while i<=10:
#     print(i,end=" ")
#     i+=1


# i=1
# sum=0
# while i<=10:
#     sum+=i
#     i+=1
# print(sum,"is the sum of first ten natural numbers")

# i=1
# pro=1
# while i<=5:
#     pro*=i
#     i+=1
# print(pro,"is the product of first ten natural numbers")


# num=int(input("enter a number:"))
# i=1
# while i<=10:
#     print(f'{num} x {i} = {i*num}')
#     i+=1


# num=int(input("enter a number: "))
# i=1
# fact=1
# while(i<=5):
#     fact*=i
#     i+=1
# print(fact,"is the factorial of the number",num)


# num=int(input("enter a number: "))
# i=5
# fact=1
# while(i<=5):
#     if (i>=1):
#         fact*=i
#     else:
#         break
#     i-=1
# print(fact,"is the factorial of the number",num)



#write a python program to get the sum of first n natural numbers using while loop
# sum=0
# num=int(input("enter a number: "))
# i=1
# while (i<=num):
#     sum+=i
#     i+=1

# print(sum)


# Write a Python while loop to find the sum of the digits of a given number.


# num = int(input("Enter a number: "))
# sum_of_digits = 0
# while num > 0:
#     sum_of_digits += num % 10
#     num //= 10
# print("Sum of digits:", sum_of_digits)

# # Write a Python while loop to reverse the digits of a number.


# num = int(input("Enter a number: "))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //= 10
# print("Reversed number:", reversed_num)


# Write a Python while loop to print the Fibonacci series up to a given number.


# n = int(input("Enter how many numbers in fibbnocci series you want: : "))
# a, b = 0, 1
# while a<= n:
#     print(a, end=" ")
#     a,b =b ,a+b

# Write a Python while loop to find the largest digit in a given number.


# num = int(input("Enter a number: "))
# largest_digit = 0
# while num > 0:
#     digit = num % 10
#     if digit > largest_digit:
#         largest_digit = digit
#     num //= 10
# print("Largest digit:", largest_digit)

# Write a Python while loop to count how many times a specific digit appears in a given number.


# num = int(input("Enter a number: "))
# digit_to_count = int(input("Enter the digit to count: "))
# count = 0
# while num > 0:
#     if num % 10 == digit_to_count:
#         count += 1
#     num //= 10
# print(f"The digit {digit_to_count} appears {count} times.")

# Write a Python while loop to calculate the sum of squares of all numbers from 1 to a given number.

# num = int(input("Enter a number: "))
# sum_of_squares = 0
# i = 1
# while i <= num:
#     sum_of_squares += i ** 2
#     i += 1
# print("Sum of squares:", sum_of_squares)

# Write a Python while loop to reverse a string.


# string = input("Enter a string: ")
# reversed_string = ""
# i = len(string) - 1
# while i >= 0:
#     reversed_string += string[i]
#     i -= 1
# print("Reversed string:", reversed_string)



# collection data types--list, set, tuple, dictionary

# list --multiple data types store, duplicates allowed, ordered, mutable


a=list()
a=[10, 20, 100.7, 'hello',True, False, 'hello',20, 10, 100.7]
# print(type(a))


# list methods
# a.append('python')
# a.append('hai')
# a.clear()
# d=a.copy()
# print(d)
# print(a.count('hello'))
# print(a.index(False))

# f=['a','b',False]
# g='hai dear anusha'
# print(g.split())

# a.extend(g)
# f.insert(1,'anusha')


# f.pop()
# f.remove('b')



# f.reverse()

# f=[100,0, -10, 20, 70, 800, -120]
# # f.sort()
# f.sort(reverse=True)
# print(f)




f=['xray','apple','none','put']
f.sort()
print(f)

# d=[10,20,30,40]
# h='hai'

# d.insert(2,h)
# print(d)














