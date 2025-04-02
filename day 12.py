#remove one element from tuple
# a=(1,2,3,4,5,6,7,8,9,10)
# a=list(a)
# del(a[0])
# a=tuple(a)
# print(a)

#loop the tuple using for loop
# a=(1,2,3,4,5,6,7,8,9,10)
# for i in range(len(a)):
#     print(a[i],end=" ")

#loop the tuple using while loop
# a=(1,2,3,4,5,6,7,8,9,10)
# i=0
# while i<len(a):
#     print(a[i],end=" ")
#     i+=1

#join two tuple ( addition opertaor)
# a=(1,2,3,4,5)
# b=("hello","hai")
# print(a+b)
# print(a*3)
#how to reverse a tuple
# a=(1,2,3,4,5,6,7,8,9,10)
# a=a[::-1]
# print(a)

# packing a tuple
a= (1,2,3,4)
print(a)

#unpacking of tuple
a=('hai','hello','yes','no','hi','king')
(*red,black,pink,green) = a
print(black)
print(red)
(red,black,pink,*green) = a
print(green)
print(red,black,pink,green)

#how to print a single value tuple
a=()
a=list(a)
for i in range(1,50):
    if i==50:
        a.insert(i)
a=tuple(a)
print(a)

# a=(50,)
# print(a)

# a=(10,20,30,30,40,50)
# print(a.count(30))

# a=(60,10,20,30,30,40,50)
# a=list(a)
# a.sort()
# print(a[0],"is the minimum value in the tuple")
# a=tuple(a)
# print(a)

# a=(10,20,30,30,40,50)
# b= min(a)
# print(b,"is the minimum value in the tuple")

# a=(10,20,30,30,40,50)
# b=max(a)
# print(max(a),"is the maximum value in the tuple")

# a=(10,20,30,30,40,50)
# a=list(a)
# a.sort()
# print(a[::-1])
# print(a[0]," is the maximum value in tuple")
# a=tuple(a)
# print(a)

# a=(1,2,3,4)
# b=(1,2,3,4)
# if a==b:
#     print("the two tuple are equal")
# else:
#     print("tuple are not equal")


# a=(1,2,3,4,5)
# sum=0
# for i in range(len(a)):
#     print(i)
#     sum= sum+i
# print()

# a=(1,2,3,4)
# print(sum(a))
# print(sum(a)/len(a))

# a=(input("enter a number:"))
# length=len(a)
# for i in range(length) :
#     for j in range(length):
#         if i==j or i+j==length-1:
#             print(a[j],end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# mylist =("car","cat","bat","ball")
# prefix="ca"
# for i in mylist:
#     if prefix in i:
#         print(i,end=" ")


