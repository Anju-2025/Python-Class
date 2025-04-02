# original_list = [1, 2, 3, 4, 5]
# reversed_list = []

# for item in original_list:
#     reversed_list.insert(0, item)  

# print(reversed_list)


# input_list=[10,20,30,40,10,20,30,40,50]
# unique_list = []
    
# for item in input_list:
#     if item not in unique_list:
#         unique_list.append(item)
    
# print(unique_list)

# # d=[]
# # for i in range(1,21):
# #     if i<=5:
# #         print(i)
# #     else:
# #         break

# # print(d)



# # for i in range(1,11):
# #     if i>5:
# #         if i==7:
# #             print(i)
# # #         continue
# # k=[]
# # d=[10,20,30,40,50]
# # for i in d:
# #     k.insert(0,i)
# # print(k)


# h=["hai","hello","and"]
# f=h[-1]

# # num=int(input("enter a number: "))
# d=[10,20,30,40]
# # d.insert(2,num)
# d.insert(2,f)
# print(d)

# sum=0
# pro=1
# f=[10,20,30,20]
# for i in f:
#     sum+=i
#     pro*=i
# print(sum,pro)


# d=[1000,20,90,50,0,50,50]
# max=d[0]
# min=d[0]
# count=0
# for i in d:
#     if (i>max):
#         max=i
#     if (i<min):
#         min=i
#     if (i==50):
#         count+=1

# print(max,"is the max number in the list")
# print(min,"is the min  number in the list")
# print(count,"is the count of the number 50")

# k=[]
# sum=0
# f=[1,2,3,4,5]
# for i in f:
#     sum+=i**2
#     k.append(i**2)
# print(k)
# print(sum)


# k=[]
# f=[10,-10,20,-100,300]
# for i in f:
#     if (i<0):
#         continue
#     else:
#         k.append(i)
# print(k)

# l1 = [1, 2, 3, 4, 5]
# l2 = [4, 5, 6, 7, 8]

# common_elements = []

# for element in l1:
#     if element in l2:
#         common_elements.append(element)

# print("Common elements:", common_elements)

# d=[10,90, 80, 56, 35]


# largest = second_largest = None
# smallest = second_smallest = None
# for num in d:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num
        
#     if num < smallest:
#         second_smallest = smallest
#         smallest = num
#     elif num < second_smallest and num != smallest:
#         second_smallest = num

# print("Second largest number:", second_largest)
# print("Second smallest number:", second_smallest)


# sum=0
# d=[10,20,30,40]
# for i in d:
#     sum+=i
# print(sum)

# d=[10,-200,130,440, 800, -12]
# max_num=d[0]
# min_num=d[0]
# for i in d:
#     if (i>max_num):
#         max_num=i
#     elif(i<min_num):
#         min_num=i
# print(max_num,'is the largest number in the list')
# print(min_num,"is the minimum number in the list")

# check whether a number is amstrong or not
# 153 ---3---3**3 + 5**3 + 1**3 =27 + 125  + 1 = 153
# num=int(input("enter a number:"))
# org_num=num
# length=len(str(num))
# sum=0
# while(num>0):
#     digit=num%10
#     sum+=digit**length
#     num//=10
# if (sum==org_num):
#     print(org_num,"is an amstrong number")
# else:
    # print(org_num,"is not an amstrong number")


# check whether a string is palindrome or not
# madam, level,malayalam
# str1=input("enter a string: ")
# if str1==str1[::-1]:
#     print(str1,"is a plaindrome string")
# else:
#     print(str1,"is not a plaindrome number")


# d='hello'
# print(d[::-1])
# d="hello"
# # print(d[0])
# # print(d[1:3])
# print(d[0:])
# print(d[:5])
# print(d[:])
# print(d[::-1])


# check whether a number is palindrome or not
# num=int(input("enter a number: "))
# org_num=num
# reverse=0
# while(num>0):
#     digit=num%10
#     reverse=reverse*10 + digit
#     num//=10

# if (reverse==org_num):
#     print(org_num,"is a perfect palindrome number")
# else:
#     print(org_num,"is not palindrome")


# d=[1221, 1220, 141, 140, 1331, 90]


# # get a fibnocci series 
# 0-1-1-2-3-5-8-13
# # a=0, b=1
# # 1==0+1 (a+b)
# # 2=(1+1)


# get fibnocci series using while loop
terms_req=int(input("enter a number: "))
a=0
b=1
while(a<terms_req):
    print(a)
    a,b=b,a+b



# get fibnocci series using for loop
terms_req=int(input("enter a number: "))
a=0
b=1
for i in range(terms_req):
    print(a)
    a , b = b, a+b
   
