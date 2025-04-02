# # List comprehensions in Python are a concise way to create lists. They allow you to generate 
# # a new list by applying an expression to each item in an existing iterable (such as a list or range) 
# # and can include conditional 
# # statements for filtering





# k=[]
# for i in range(1, 11):
#     if (i%2==0):
#         k.append(i)
# print(k)




print([ i for i in range(1,11) if i%2==0])




# # print([i  for i in range(1, 11) if i%2==0])



# # syntax

# # new_list = [expression for item in iterable if condition]

# # square of numbers

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers if x%2==0]
print(squares)

# # for i in numbers:
# #     print(i**2)


# d='hello'
# l=[i for i in d if i!='h']
# print(l)


# d=[ i for i in range(1, 21) if i%2==0]
# print(d)




# filtering even numbers

# numbers = [1, 2, 3, 4, 5]
# squares = [x**2 for x in numbers if x%2==0]
# print(squares)

# # using function within list comprehension

# words = ["hello", "world", "python"]
# print([i.upper() for i in words])


# # # nested list comprehension

# table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
# print(table)

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i*j)

# k=[10, 20, 30]
# f=sum([i for i in k])
# print(f)

# k=[]
# for i in range(1, 21):
#     if (i%2==0):
#         k.append(i**2)
# print(k)


# list comprehension ---single line

# d=[ i**2 for i in range(1, 21) if i%2==0]
# print(d)

# s=[10,20,30, 25, 19, 17]
# print(sum(s))
# print(min(s))
# print(max(s))


# f=sum([ i for i in s if i%2==0])
# print(f)

# d=[1, 2, 3, 4, 5]
# for i in d:
#     for j in d:
#         print(i*10+j,end=' ')

# 11=1*10+1
# 53=5*10+3

# d=['1','2','3','4','5']
# for i in d:
#     for j in d:
#         print(i+j,end=' ')


# d='hello'
# g='world'

# print(d+" "+g)

# l=[]
# for i in range(1, 21):
#     if (i%2==0):
#         l.append(i**2)

# print(l)
# list comprehension
# [expression for item i iterable if condition]
# g=[ i**2 for i in range(1, 21) if i%2==0]
# print(g)

# d=[101, 11, 20, 30, 40]
# # print(sum(d))
# # print(min(d))
# # print(max(d))

# k=sum([ i for i in d if i%2==0])
# print(k)


# d=['1', '2', '3', '4', '5']
# for i in d:
#     for j in d:
#         print(i+j, end=" ")

# d=[1, 2, 3, 4, 5]
# for i in d:
#     for j in d:
#         print(i*10+j, end=' ')

    
# 11=1*10+1
# 12=1*10+2

# 54=5*10+4

# k=[]
# for i in range(1, 21):
#     if (i%2==0):
#         k.append(i**2)
# print(k)

# print([i**2 for i in range(1, 21) if i%2==0])


# list comprehension

# [expression for item in iterable if condition]


# s=['1','2','3','4','5']
# for i in s:
#     for j in s:
#         print(i+j, end=' ')

# s=[1, 2, 3, 4, 5]
# for i in s:
#     for j in s:
#         print(i*10+j, end=' ')

# 11=1*10+1
# 12=1*10+2

# 43=4*10+3
# 52=5*10+2



# f='hello dear python'

# print([ i[0] for i in f.split()])


# for i in range(1,4):
#     for j in (1,3):
#         print((i,j),end='')


# new_list=[]
# f=['hello','python','course','sttudent']
# for i in f:
#      new_list.append(i[0])
# print(new_list)


# print([i[0] for i in f ])



# num=int(input("enter a number: "))
# for i in range(2, num):
#     if (num%i==0):
#         break
# else:
#     print(num,"is a perfect prime number.")



# if not [i for i in range(2, num) if num % i == 0]:
#     print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")


# syntax

# def function_name():
#     # block of codes
#     pass
# function_name()




# def show(a, b):
#     print(a+b)
# show(10, 20)
# show('hello','abhi')

# 10--argument
# a--parameter

# def display(a):
#     for i in a:
#         if (i%2==0):
#             print(i)
    

# d=[10,25, 31, 40]
# display(d)


# d=[10,20,30]
# print(sum(d))

# g={}
# keys=['name','age','place']
# values=['ammu',12,'tvm']
# for i in range(len(keys)):
#     g[keys[i]] = values[i]

# print(g)


