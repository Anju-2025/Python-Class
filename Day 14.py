#merge two python dictionaries into one
# d1={"ten":10,"twenty":20,"thirty":30}
# d2={"thirty":30,"forty":40,"fifty":50}
# d1.update(d2)
# print(d1)
# print(d1|d2)
# d3=d1.copy()
# d3.update(d2)
# print(d3)


#check 200 in s1
# s1={"a":100,"b":200,"c":300}
# print(200 in s1.values())

#find mark of history
# sample ={"class":{"student":{"name":"mike","marks":{"physics":70,"history":80}}}}
# print(sample["class"]["student"]["marks"]["history"])
# sample={"class":{"student":{"name":"mike","marks":{"maths":89,"english":90}}}}
# print(sample["class"]["student"]["marks"]["english"])


# #change salary of ammu to 8500
# d= {"emp1":{"name":"John","salary":7500},
#    "emp2":{"name":"emma","salary":8000},
#     "emp3":{"name":"ammu","salary":5000}}
# d["emp3"]['salary'] = 7000
# print(d)

#python program to convert number into words using list
# A=["","one","two","three","four","five","six","seven","eight","nine"]
# C=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","ninteen"]
# B=[" "," ","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty","hundred"]
# n=int(input("enter a number:"))
# if n<=10:
#     print(A[n])
# elif n>10 and n<20:
#     y=n%10
#     print(C[y])
# elif n>20 and n<100:
#     ones=n%10
#     tens=n//10
#     if ones==0:
#         print(B[tens])
#     else:
#         print(B[tens] + A[ones])



A=["","one","two","three","four","five","six","seven","eight","nine","ten"
   ,"eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","ninteen"]
B=[" "," ","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty","hundred"]
n=int(input("enter a number:"))
r=n%10
if n in range(1,20):
        print(A[n])
elif n in range(20,100):
     r=n%10
     q=n//10
     print(B[q]+A[r])
else: 
       n==100
       print(B[10])

#python program to convert numbers into words using dictionary

# A = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven"
#      ,12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen"
#      ,16:"sixteen",17:"seventeen",18:"eighteen",19:"ninteen"
#      ,20:"twenty",30:"thirty",40:"forty",50:"fifty"
#      ,60:"sixty",70:"seventy",80:"eighty",90:"ninty",100:"hundred"}
# n=int(input("enter a number:"))
# if n<=100:
#     if n in A:
#         print(A.get(n))
#     else:
#         r=n%10
#         q=n//10
#         q=q*10
#         print(A.get(q),A.get(r))
# else:
#     print(n,"enter a number<=100")


