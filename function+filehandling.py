# def count_lines(filename):
#     with open(filename, "r") as file:
#         return sum(1 for line in file)

# # Test
# print(count_lines("ann.txt"))


# d=[10,20,30]
# print(sum(d))
# print(min(d))
# print(len(d))

# def sum_function(a, b, c,d):
#     print(a**2, b, c, d)

# sum_function(10, 20,'hello', [10,20])
# 10--argumnet
# a=parameter

# def new(a, b):
#     print(a+b)
#     return a+b


# print(new(10,20))

# scope--global, local


# a=10
# def new():
#     global b
#     b=20
#     print(a)
#     print(b)

# new()
# print(b)


# arbitratry argument (*args)
# def new(*a):
#     print(a)
# new(10,20,30)

# keyword argumnet (kwargs)
# def new(b, c , a):
#     print(b)
#     print(a+c)
# new(a=10,b=20,c=30)


# # arbitrary keyword argumnet (**kwargs)
# def new(**k):
#     print(k)
  

# new(a=10,b=20,c=30)


def factorial(k):
    fact=1
    for i in range(1,num+1):
        fact*=i
        print(fact,'is the factorial of the number',num)
num=int(input('enter a number:'))
factorial(num)


