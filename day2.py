# arithametic

# a=10
# b=25
# print(a+b)




# a=100
# b=20
# print(a-b)

# a=100
# b=5
# print(a*b)

# a=100
# b=20
# print(a/b)

# a=25
# b=4
# print(a%b)

# a=100
# b=21
# print(a//b)

# a=10
# b=2
# print(a**b)


# comparison


# a="apple"
# b="APPLE"
# print(a==b)

# a=20
# b=30
# print(a!=b)



# a=10
# b=20
# print(a>=b)

# a=10
# b=27
# print(a<=b)

# a=10
# b=20
# print(a>b)


# relational operators



# a=10
# a+=2
# print(a)

# a=20
# a*=2
# print(a)

# a=50
# a/=5
# print(a)

# a=20
# a//=3
# print(a)

# a=25
# a**=2
# print(a)


# Logical operators

# a=10
# b=2
# c=5
# print(a>b and a>c)
# print(b<a or c<b)
# print(not(a>b))

# membership operators in not in

# a="Home"
# print("m" in a)
# print("d" not in a)


# identity operators is is not

# b=10
# c=20
# print(b is c)
# print(b is not c)


# a=100
# b=60
# c=25
# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("b is greater")
# else:
#     print("c is greater")

# Exercise:1

# p=int(input("enter a number,k"))
# if p==1:
#     print('monday')
# elif p==2:
#     print('tuesday')
# elif p==3:
#     print('wednesday')
# elif p==4:
#     print('thursday')
# elif p==5:
#     print('friday')
# elif p==6:
#     print('saturday')
# elif p==7:
#     print('sunday')
# else: 
#     print('invalid')

#Exercise: 2

# p=float(input("enter a number,k"))
# if p > 0:
#     print("It is a positive number")
# elif p==0:
#     print("It is zero") 
# else:
#     print("It is a negative number")    

# #Exercise: 3

# p=int(input("enter a number, k"))
# if p % 2 ==0:
#     print("It is an even number")
# else:
#     print('It is an odd number')    

# Exercise:4

# p=int(input("enter a number,k"))
# factorial=1
# if p<0:
#     print("Factorial does not exist")
# if p==0:
#     print("The factorial is 1")  
# else:
#     for i in range (1,p+1):
#         factorial*=i
# print("factorial is",factorial)  



# for i in range(1,11):
#     print(i,end=' ')

# k=[10,20,30,40]
# j=(10,20,30)
# for i in j:
#     print(i)

# for i in range(1,21):
#     if (i%2==0):
#         print(i,"is an even number")
#     else:
#         print(i,"is an odd number")

# d="hospital case and accident"
# count=0
# for i in d:
#     if ('a' in i):
#         count+=1
# print(count)

d=[1,2,3,4,5]
sum=0
pro=1
for i in d:
    sum+=i
    pro*=i
print(sum,"is the sum of numbers in the given list")
print(pro)










# a=[10,20,30,40]

# # a=sum(a)


# print(min(a))
# print(max(a))
# d=sum(a)
# print(d)




# Exercise:5

# p=int(input("Enter a number:"))
# if p%2==0 and p%3==0:
#     print("The number is divisible by 2 and 3")
# elif p%2==0 and p%3>0:
#     print("The number is divisible by 2 only")  
# elif p%3==0 and p%2>0:
#     print("The number is divisible by 3 only")      
# elif p%2>0 and p%3>0:
#     print("The number is not divisible by 2 and 3")    

