# a="hello"
# print(a)
# print(type(a))

# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[-1])
# print(a[-2])
# print(a[-3])
# print(a[-4])
# print(a[-5])
# print(a[:])
# print(a[0:])
# print(a[:5])
# print(a[1:5])
# print(a[-3:-1])
# print(a[-4:-1])
# print(a[::-1])
# print(a[0:5:2])

# indexing and slicing

# my world of python is fantastic

# fan
# thon
# d of p
# r
# tic

# f=[10,20,30,40,50,60]
# print(f[0:4])

# k=("hai","hello",False,9, 89)
# print(k[3])

# list ---methods
# ----------multiple datatypes, duplicates allow
d=[10,"hai",False]
# print(d)
# d.append("hello")
# d.clear()
# h=d.copy()
# print(h)


# print(d.count(10))
# print(d.index("hai"))


# k=[90,99, 89, 90]
# l=(100,99)
# d.extend(k)
# d.extend(l)
# d.insert(0,"python")
# print(d.pop())
# # d.pop()
# d.remove(False)
# # d.reverse()
# p=[10,100,0, -100, -200, 67]
# k=["zen",'pen','ball','window','BALL','APPLE','and']
# # o=["hai","apple",100,90, 0]
# # o.sort()
# # print(o)
# k.sort()
# print(k)
# p.sort()
# p.sort(reverse=True)
# print(p)


h=['hai',True,10,False,"and",100,100.8]




#Exercise:1
# i=str(input("enter a word"))
# ing=str
# if len(i)<=2:
#         print(i)
# elif len(i)>=2:
#         print(i+"ing")
#         if("ing"in i):
#                 p= i.replace("ing","ly")
#                 print(p)
# else:
#     print(i)

# print(sum([10,20,30]))
# print(max([10,20,30]))
# print(min([10,20,30]))
# print(len('arya'))
# print(len([10,20,30]))
    
#Write a program to count the length of string without using inbuilt function.

# i=str(input("enter a word"))
# print(len(i))

# i=str(input("enter a word: "))
# count=0
# for j in i:
#     count+=1
# print("Number of letters in the word is: ", count)


# write a program to count the length of letter, digit and spl character without using inbuilt function.


# string=str(input("enter a word: "))
# alpha_count=0
# digit_count=0
# spl_char_count=0
# for i in string:
#     if i.isalpha():
#         alpha_count+=1
#     elif i.isdigit():
#         digit_count+=1
#     else:
#         spl_char_count+=1
# print("Number of letters is: ",alpha_count)
# print("Number of digits is: ",digit_count)
# print("Number of spl character is: ",spl_char_count)





#write a program to accept string and display total  number of alphabets
# word=str(input("enter a word: "))
# count=0
# for i in word:
#     count+=1
# print("no of letters is: ",count)

#write a program to count the number of lowercase and uppercase character in a string accepted from the user

# i=(input("enter a string:"))
# count1=0
# count2=0
# for a in i:
#     if a.isupper():
#         count1=count1+1
#     elif a.islower():
#         count2=count2+1
# print("The number of upper case letter is: " )
# print(count1)
# print("The number of lower case letter is:")
# print(count2)

# x="Xn@12mNh978#"
# c=0
# for i in x:
#       if i.isdigit()==True:
#           c=c+1
# print("Number of alphabets:",c)

# X="236#Vhbitdmal"
# a="aeiouAEIOU"
# c=0
# for i in X:
#        for j in a:
#               if i==j:
#                      c=c+1
# print("No of vowels: ",c)
              
              

# x="restart"
# print(x.replace("r","k"))

# x="hello"
# p=(x.rfind[3])
# # c=x.replace(p,"#")
# print(p)

# X="ABIOP390@#!"
# S="aeiouAEIOU"
# c=0
# for i in X:
#     for j in S:
#         if i==j:
#             c=c+1
# print("vowels:",c)