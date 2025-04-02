# x=input("enter a number: ")
# length=len(x)
# for i in x:
#     for j in x:
#         if i==j or i+j==length-1:
#             print(x[i],end=" ")
#         else:
#             print(" ")
# print()
#                         #TUPLE

# a= (1,2,3,4,2,3,2,5,3,2,"hello",True,"hai")
# print(a)
 # methods in Tuple
# print(a.count(2)) 
# print(a.index(2))
# print(a[4])
# print(a[::-1])
# print(type(a))
#how to change any element in a tuple to another element. (convert to list, assign new value, then convert to tuple)
# a= (1,2,3,4,5)
# a=list(a)
# a[0]=6
# a= tuple(a)
# print(a)
# tup=("hai",5,True,30.5)
# li=list(tup)
# li[3]=50.5
# tupp=tuple(li)
# print(tupp)
# print(tup)
# print(li)

# l=[1,2,3,4]
# tup=tuple(l)
# print(tup)
# print(type(tup))
# print(type(l))

# tup=(1,2,3,4,"hi")
# li=list(tup)
# print(type(tup))
# print(type(li))
# print(li)

# tup=("hello","python","java",60,False,"python")
# print(tup.count("python"))
# print(tup.index(False))
# print(tup.index("python",3))
# print(len(tup))

# x=("apple",)
# print(type(x))

# x=("hello",60,True,"python")
# print(x[4])
# print(x[-4:-2])
# if True in x:
#     print("yes")
# else:
#     print("not found")
# li=list(x)
# li.append("java")
# li[3]="kiran"
# li.remove("hello")
# x=tuple(li)
# print(x)

# y=(2,3,4)
# x+=y

# print(x)

#                                unpacking of tuple

# x=(10,20,30,40,50,"red","yellow","green")
# (red,green, *yellow)=x
# print(yellow)
# print(red)
# # #                                       for loop
# for i in x:
#     print(i,end=" ")
#                                 range and index looping
# tuple=("hello","hai","python","java")
# for i in range(len(tuple)):
#     print(tuple[i])

# while loop
# tuple=("hello","hai","python","java")
# i=0
# while i<len(tuple):
#     print(tuple[i])
#     i+=1
# # #                              join tuples

# h=["hai","hello","word","here","there"]
# print("here" in h)

# tup1=(2,4,6,8)
# tup2=(1,3,5,7)
# # tup3=tup1+tup2
# # print(tup3)
# # # print(tup1+tup2)
# # print(tup1*2)
# # print(tup2*3)
# print(min(tup1))
# print(max(tup2))
# x=("hai","hello","word","here","there")
# print("here" in x)
# print("words" in x)

# x=(1,2,3,4,5)
# sum=0
# for i in x:
#     sum+=i
# print("sum of elements is: ",sum)

# x=(1,2,3,4,5)
# print(len(x))
# mul=1
# for i in x:
#     mul*=i
# print("product of elements is: ",mul)

# x=(1,2,3,4,5)
# mul=1
# index=0
# while index<len(x):
#     mul*=x[index]
#     index+=1
# print("product of elements is: ",mul)


# set  - methods
# d={10,True,"hai",100.5}
# d.add("python")
# d.remove("hello")
# d.discard("hello")
# print(d)
# d.pop()

# p1={1,2,3,4,5,6}
# p={3, 4}
# q={8, 9}
# p2={5, 6, 7, 8, 9 , 10}

# print(p1.union(p2))
# print(p1.intersection(p2))
# print(p1.symmetric_difference(p2))
# print(p1.difference(p2))
# print(p2.difference(p1))

# print(p.issubset(p1))
# print(p1.issuperset(q))

# d={'name':'sebin','age':10,'place':'tvm'}
# print(d['place'],"is the place of sebin", d['age'],'is years old')
# d['gender']='male'
# print(d)

# d.update({'name':'soorya'})
# print(d)

# print(d.keys())
# print(d.values())
# print(d.items())


# print(d['age'])
# print(d.get('age'))


# d.pop('age')
# d.popitem()

# print(d)


# for while

# for item in iterable

# for i in range(1,11):
#     print(i,end=' ')

# f=[10,20,30]

# g=[]

# for i in f:
#     g.append(i**2)
# print(g)

# f=(10, "hai", True, 100.6, 10, 10)
# print(type(f))
# # print(f.count(10))
# # print(f.index("hai"))

# f=list(f)
# print(type(f))
# f.append("python")
# f=tuple(f)
# print(f)



# h="hello dear python"

# print(h[0:])
# print(h[:17])
# print(h[:])
# print(h[::-1])

# h, l, 0, d, a, 


# print(h[0])
# print(h[0:16:2])

# print(h[-1])
# print(h[-11:-7])

# d="the development in the field of python"

# ment, the, field, dev, in, e


h="hello dear python"
# print(h.capitalize())
# print(h.title())
# print(h.upper())


j="35345"
# print(j.islower())
# print(j.isupper())
# print(j.lower())
# print(j.isalpha())
# print(j.isalnum())
# print(j.isdigit())

# l="hellodear python"
# print(l.split())

# l="Hello"
# print(l.center(9,"*"))
# print(l.casefold())
# print(l.endswith('p'))
# print(l.startswith('h'))


h="hello dear world"
g=h.split()
print(g)







