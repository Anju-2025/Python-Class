# a=[]
# i=1
# while i<=20:
#     if (i%2==0):
#         a.append(i)
#     i+=1
# print(a)


l1=[]
i=10
while (i<=10):
    if (i>0):
        l1.append(i)
    else:
        break
    i-=1

print(l1)

# a=[]
# i=10
# while i>=1:
#     a.append(i)
#     i-=1
# print(a)

# a=[]
# i=2
# while i<=10:
#     a.append(i)
#     i+=2
# print(a)





# a=[10, 30, 20, 70, 5]
# # a.pop()
# # print(a)
# # # print(a)
# a.reverse()
# print(a)
#                        #BREAK & CONTINUE
# i=0
# while i<10:
#     i+=1
#     if i==9:
#         continue
#     print(i, end=" ")

# for i in range(1,21):
#     if i%3==0:
#         continue
#     print(i,end=" ")

    

# i=0
# while i<10:
#     i+=1
#     if i==3:
#         continue
#     elif i==5:
#         continue
    
#     print(i,end=" ")

#python program to count number of digits in a number, input.

# p=int(input("enter a number:"))   
# count=0
# while p>0:
#     p//=10
#     count+=1
# print(count) 

# python program to check a number is palindrome or not

# p=int(input("enter a number:")) 
# q=p
# reverse=0
# while p>0:
#     x=p%10
#     reverse = reverse*10 + x
#     p//=10
# print(reverse)
# if reverse==q:
#     print(q,"is palidrome")
# else:
#     print(q,"is not palindrome")
       
# p=int(input("enter a number: "))
# var=p
# reverse=0
# while p>0:
#     x=p%10
#     reverse=reverse*10+x
#     p//=10
# if var==reverse:
#     print(var,"is plaindrome")
# else:
#     print(var,"is not palindrome")

# def is_palindrome(n):
#     return str(n)==''.join(reversed(str(n)))

# n=int(input("enter a number: "))

# if is_palindrome(n):
#     print(n,"is plaindrome")
# else:
#     print(n,"is not palindrome")





# def is_palindrome(num):
#     org_num=str(num)
#     rev_num=org_num[::-1]
#     return org_num==rev_num

# num=int(input("enter a number: "))
# if is_palindrome(num):
#     print("palindrome")
# else:
#     print("not palindrome")

# n=int(input("enter a number: "))
# var=n
# reverse=0
# while n>0:
#     reverse=reverse*10+ n%10
#     n//=10
# if var==reverse:
#     print("palindrome")
# else:
#     print("not palindrome")

# p=int(input("enter a number:"))  
# x=p
# z=p
# arm=0
# count=0
# while p>0:
#     count+=1
#     p//=10
# print(count)
# while x>0:
#     e=x%10
#     arm=arm + e**count
#     x//=10
# print(arm)
# if z==arm:
#     print("it is an armstrong number")
# else:
#     print("it is not an armstrong number")




# num=int(input("enter a number: "))
# x=num
# reverse=0
# while num>0:
#     r=num%10
#     reverse=reverse*10 + r
#     num//=10
# print(reverse)
# if reverse==x:
#     print(x,"palindrome")
# else:
#     print(x,"not palindrome")


# num=int(input("enter a number: "))
# x=num
# y=num
# arm=0
# count=0
# if num>0:
#     count+=1
#     num//=10
# print(count)
# while x>0:
#     p=x%10
#     arm=arm + p**count
#     x//=10
# print(arm)
# if arm==y:
#     print(y,"is armstrong")
# else:
#     print(y,"is not armstrong")


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

   

# y={2,3,4,5}
# y.remove(2)
# print(y)
# y.add(5)
# print(y)
