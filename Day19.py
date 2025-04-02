# File Handling

# # Files -  to open a file
# #Type of modes, in read, write, append and create.
# syntaxf=open("file name","mode")  
# file=open('nandu.txt','r')
# print(file.read())
# print(file.readlines())
# print(file.readline())
# print(file.readline())
# file.close()
# print(file.read())
# # # # 
# overwrite content in case of already created file
 #newly add content in not existing file


# file=open("nandu.txt","w")  
# file.write("helloooooooo")

# file=open('nandu1.txt','w')
# file.write('hai nandu!')



# file=open("nandu2.txt","a")  
# file.write("*8**")


# file=open('nandup.txt','x')
# file.write('haiaaaaaaaaaaa')

# f=open("sebin1.txt","w")  
# f.write("helloooooooo sebin")

# existing ---file handling--read, write, append

# non existing---write, append, create




# f=open("minnu2.txt","w")  
# f.write("haiiiiiiiiiiiii")
# print(f.read())
# f.close()
# f.write("ammu")

# f=open("abh4.txt","x")

# f.write("Course of python")




# existing file --read, write, append
# non existing file - write, append, create
# MODES -- READ, WRITE, APPEND, CREATE
# r, w, a, x
# variable=open('filename','mode')
# variable.close()


# file=open("minnu4.txt","x")
# file.write("aparna")


# existing --read, write, append
# non existing - write, append, create


# f=open("sebin2.txt","a")                #add at last of already created file                                    # create and append in not exiting file
# f.write('darling')
# f.close()

# f=open("sebin3.txt","x")    
# f.write("haiiiiiiii")      #error for already existing File:        #create new, if doesnt exist   
# f.write("Happy world")
# f.close()


# f=open("hello.txt","r")
# k=f.readlines()
# print(k)
# p=max(k)
# print("maximum number",p)
# # d=min(k)
# # print("minimum number",d)



# f=open("hello.txt","w")       
# f=open("2.txt","w")                          
# f.write("python world")
# f.close()

# score = int(input("Enter the score: "))
# if (score >= 90 and score <=100):
#     print("A")
# elif (score >= 80 and score <90):
#     print("B")

# File handling and Loop Combination Questions

# 1)
# file=open('minnu.txt','r')
# v=file.read()
# # print(v)
# x='python'
# count=0

# for i in v.split():
#     if (i == x):
#         count+=1
# print(count)


# alternative method without using forloop

# file = open('minnu.txt', 'r')
# v = file.read()
# x = "python"
# count = v.count(x) 

# print(count, "is the count of the string", x)


# 2) 


# file=open('minnu2.txt','a')

# for i in range(1,101):
#     if (i%2==0):
#         file.write(str(i) + '\n') 

# file.close()

# 3) 

# file=open('minnu.txt','r')
# v=file.read()

# f1=open('minnu5.txt','a')

# for i in v.split():
#     f1.write(str(i) + '\n')

# file.close()
# f1.close()


# 4)

# with open("minnu.txt", "r") as file:
#     for line in file:
#         if "error" in line:
#             print(line.strip())


# 5) 

# names = ["Alice", "Bob", "Charlie", "Diana"]
# # with open("names.txt", "w") as file:
# #     for name in names:
# #         file.write(f"{name}\n")


# # 6)

# # line_count = 0
# # with open("document.txt", "r") as file:
# #     for line in file:
# #         line_count += 1
# # print(f"The file has {line_count} lines.")


# # 7)

# # with open("text.txt", "r") as file:
# #     lines = file.readlines()

# # with open("text.txt", "w") as file:
# #     for line in lines:
# #         file.write(line.replace("old", "new"))


# # file=open('text.txt','r')
# # p=file.readlines()

# # file1=open('text.txt','w')
# # for i in p:
# #     file1.write(i.replace('old','new'))





# d=[10, 20, 30, 40, 50, 60, 70]

# # output 1 = [40]
# # output 2 =[50,60]
# # output 3 =[20, 40, 60]

# s="hello dear python program"

# # output 1= 'dear'
# # output 2 = 'python'
# # output 3 = 'on' 
# # output 4 = 'll'

# class Dog:
#     name = ""
#     age = 0
#     breed = ""

  
#     def bark(self):
#         print(f"{self.name} says woof!")

#     def age_in_human_years(self):
#         return self.age * 7

    
#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}")

# dog1 = Dog()
# dog1.name = "Buddy"
# dog1.age = 3
# dog1.breed = "Golden Retriever"


# print(dog1.name) 
# print(dog1.age)   


# dog1.bark()  
# print(f"{dog1.name}'s age in human years: {dog1.age_in_human_years()}")  
# dog1.display_info()  


# for i in range(1,11):
#     print(i)

i=1
while(i<=10):
    if (i%2==0):
        print(i)
    i+=1


    # 10, 9, 8, --1