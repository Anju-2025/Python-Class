# a=[10, 20, 30, 40, 50, 60]
# a[0]=5
# print(a)
# a[1:3] =[6,8]
# print(a)
# a[1:4]=[100,200]
# print(a)
# a[1:3]=[1,2,3,4]
# print(a)
# print(60 in a)

#Methods in List - append, pop, insert, extend, clear,remove,sort

# a=[10, 20, 30, 40, 50]
# a.append(100)
# print(a)
# a.pop()
# a.pop(0)
# print(a)
# r=a.pop(0)
# print(r,"pop value")
# print(a)
# a.insert(1,1000)
# print(a)
# b="hello"
# a.extend(b)
# print(a)
# a.remove(10)
# print(a)
# del a[2]
# print(a)
# a.clear()
# print(a)
# a=["A","a","CAR","car"]
# a.sort()
# print(a)
# a=[10,0,-1,100,-12]
# a.sort()
# print(a)

                #(for,for-range,while) loops in List

# a=[10,20, 30, 40, 50]
# for i in a:
#     print(i,end=" ")

# a=[10,20, 30, 40, 50]
# for i in range(len(a)):
#     print(a[i],end=" ")

# a=[10,20, 30, 40, 50]
# i=0
# while i<len(a):
#     print(a[i])
#     i+=1

# a=[100,200,300,400,500]
# a.clear()
# # print(a)
# i=1
# while i<11:
#     print(i,end=" ")
#     b=[i]
#     i+=1
#     print(b,end=" ")

# a=[]
# b=int(input('enter a number:'))
# for b in range(1,b):
#     a.append(b)
# print(a)


# for loop ----
# print('hello'*2)

# syntax  for item in iterable --- list, tuple, string, range of numbers

# for i in range(1, 11):
#     # print('hello')
#     print(i, end=' ')


# d="helo"
# for i in d:
#     print(i)


# k=[]
# l=[]

# f=[10,20, 30, 40, 41, 21, 71]
# for i in f:
#     if (i%5==0):
#         k.append(i**2)
#     else:
#         l.append(i)

# print(k,"is the new list")
# print(l)

# even=[]
# even_count=0
# odd=[]
# d=[2, 10, 13, 14, 15, 26, 20, 31, 40, 99]
# for i in d:
#     if (i%2==0):
#         even_count+=1
#         even.append(i)
#     else:
#         odd.append(i)
# print(even, even_count)
# print(odd)



# f=[]
# for i in range(20, 41):
#     if (i%5==0):
#         f.append(i**2)
#     # else:
#     #     print(i**3, end=' ')
# print(f)


# g='hello dear python'
# count=0
# for i in g.split():
#     count+=1
# print(count,"is the number of words in the sentence")


d=[10, 20, 30, 40]
sum=0

for i in d:
    sum+=i
print(sum)