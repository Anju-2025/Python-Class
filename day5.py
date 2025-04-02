
# n=5
# p=5
# for i in range(n):
#     for j in range(n-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print(p,end=" ")
#     p-=1
#     print()

# n=5
# for i in range(n):
#     p=5
#     for j in range(n-1):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print(p,end=" ")
#         p-=1
#     print()


# n=int(input("enter a number:"))
# for i in range(2,n):
#     if n%i==0:
#         print(n, "is not a prime number")
#         break
#     else:
#         print(n,"is a prime number")

# Floyd's Triangle
# n=5
# p=1
# for i in range(n):
#         for j in range(i+1):
#             print(p,end=" ")
#             p+=1
#         print()


# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# list


# s=[40, 60, 100, 0, -45, 200, 100]
# d=["hai","hello"]
# print(s)
# print(type(s))
# s.append("hai")
# print(s)
# s.clear()
# print(s)
# a=s.copy()
# print(a)
# print(s.count(5))
# s.extend(d)
# print(s)
# print(s.index("hai"))
# s.insert(0,"anju")
# print(s)
# s.pop()
# print(s)
# s.remove("hai")
# print(s)
# s.reverse()
# print(s)
# s.sort()
# s.sort(reverse=True)
# print(s)



# print(d[0])
# print(d[0:2])
# print(d[0:5:2])
# print(d[:])
# print(d[0:])
# print(d[:8])
# print(d[::-1])
# print(d[-1])







# d=[19,100,10,20,30,40]
# d.append(False)
# d.clear()
# h=d.copy()
# print(d.count(10))
# g=[True, False]
# d.extend(g)
# print(d.index(20))
# d.insert(0,"python")
# d.pop()
# d.remove(40)
# d.reverse()

# f=["and","abi","arun","man","Abi"]
# f.sort()
# # f.sort(reverse=True)
# print(f)
# # print(d)

# d="Python language in program"
# print(d.capitalize())
# print(d.title())
# print(d.upper())
# print(d.isupper())
# print(d.islower())
# print(d.isalpha())
# print(d.isnumeric())
# print(d.isalnum())
# print(d.count('g'))
# print(d.endswith('m'))
# print(d.startswith('P'))
# print(d.find('P'))
# print(d.index('P'))
# l="girl"
# m="love"
# k="hello dear 0 h "
# # print(k.center(9,"*"))
# # print(k.replace('e','a'))
# print(k.split())

# k="arya123 "
# print(k.isalnum())
# list--mutable
# tuple--immutable
# d=(10,20,True,'hau',10,10)
# print(d.count(10))
# print(d.index(10))
# d=list(d)
# d=tuple(d)
# print(d)


# set and methods --mutiple daatatype, 
# duplicates not allow, unordered, no indexing

# s={10,20,"hai",True, 10, 100.8,0,1, False}
# # print(s)

# # s.add("python")
# # s.pop()
# # print(s)
# d={1,2,3,4,5,6}
# # k={3,4}
# j={5,6,7,8,9,10}
# print(d.union(j))
# print(d.intersection(j))
# print(d.symmetric_difference(j))
# print(d.difference(j))
# print(j.difference(d))
# print(d.issuperset(k))
# print(k.issubset(d))

f={'name':'Anju','age':10,"place":'tvm'}
# print(f['age'])
# print(f.keys())
# print(f.values())
# print(f.items())

# f['gender']='female'
# f.update({'place':'kochi'})
# print(f)
# print(f.get('age'))
# f.pop('place')
# f.popitem()
# print(f)


# d="python"
# g=[10,20,30]
# print(sum(g))
# print(min(g))
# print(max(g))
# print(len(d))

# a=10
# b=20


# d, b, m=10, 20, 30

# num=int(input("enter a number: "))
# if num%2==0:
#     print(num,"is an even number")
# else:
#     print(num,"is an odd number")

# syntax--for item in iterable

# for i in range(1,11):
#     print(i,end=' ')
# l=[]
# d=[10,20,30,40, 31,41]
# for i in d:
#     if (i%5==0):
#         print(i)
#     else:
#         l.append(i)
# print(l)


# k=[]
# for i in range(1,11):
#     k.append(i)
# print(k)

# k=[]
# m=[]
# for i in range(1,11):
#     if (i%2==0):
#         k.append(i)
#     else:
#         m.append(i)

# print(k)
# print(m)


# d="hello"
# for i in d:
#     print(i)

# k=[10,20,30,40]

# for i in k:
#     print(i)




# p="hello world"
# if ('h' in p ):
#     print('h is present')
# else:
#     print('h is not present')



score = int(input("Enter the score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")




