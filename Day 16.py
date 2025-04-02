
# PHONEBOOK USING DICTIONARY

a=int(input("\n1.add \n2.View \n3.Add/Update \n4.delete \n5.clear \n6.enter your choice:"))
pb={}
while a>0:
    if a==1:
        c={}
        name=input("enter a name: ")
        c['name']=name
        ph=[]
        g=int(input("how many numbers do you want to add as phone number:" ))
        for i in range(0,g):
            phonenumber = input("enter a number:")
            ph.append(phonenumber)
        c['phonenumber']=ph
        pe=[]
        h=int(input("how many emails you want to add:"))
        for i in range(0,h):
            email=input("enter an email:")
            pe.append(email)
        c['email']=pe
        pa=[]
        k=int(input("how many address want to add:"))
        for i in range (0,k):
            address=input("enter an address:")
            pa.append(address)
        c['address']=pa
        pb[name]=c
        print(pb)
        a=int(input("\n1.add \n2.View \n3.Add/Update \n4.delete \n5.clear \n6.enter your choice:"))
    elif a==2:
        z=input("enter a name to view:")
        print(pb)
        a=int(input("\n1.add \n2.View \n3.Add/Update \n4.delete \n5.clear \n6.enter your choice:"))
    elif a==3:
        z=int(input("what do you want to update? \n1.name \n2.phnnumber \n3.email .n4.address \n5.your choice"))
        while z>0:
            if z==1:
                name_toupdate=input("whose phone book you want to update?")
                newname=input("enter the newname: ")
                n=pb.pop(name_toupdate)
                print(n)
                pb[newname]=n
                n['name']=newname
                print(pb)
                z=int(input("what do you want to update? \n1.name \n2.phnnumber \n3.email .n4.address \n5.your choice"))
    #         if z==2:
    #             name_toupdate=input("whose phone book you want to add/update?")
    #             s=pb[name_toupdate]
    #             print(s)
    #             y= s['phonenumber']
    #             ad=int(input("select from the choice: \n1.update \n2.add \n3.update finished \n4.select your choice"))
    #             if ad==1:
    #                 g=int(input("which phonenumber you want to update?"))
    #                 phonenumber1=int(input("enter the new phonenumber:"))
    #                 y[g-1]=phonenumber1
    #                 print(y)
    #             elif ad==2:
    #                 h=int(input("how many numbers you want to add as phonenumber?"))
    #                 for i in range(0,h):
    #                     phonenumberh=int(input("enter the new phonenumber to add:"))
    #                     y.append(phonenumberh)
    #                     s['phonenumber']=y
    #                     pb[name_toupdate]=s
    #                     print(pb)
    #                     print("updation finished")
    #             break
    #     a=int(input("\n1.add \n2.View \n3.Add/Update \n4.delete \n5.clear \n6.enter your choice:"))
    # elif a==4:
    #     b=int(input("what dp you want to delete? \n1.name \n2.phonenumber \n3.email \n4.address \n5.nothing to delete \n6.select from the choice"))
    #     while b>0:
    #         if b==1:
    #             n=input("enter the name to delete: ")
    #             del pb[n]
    #             print(pb)
    #             a=int(input("\n1.add \n2.View \n3.Add/Update \n4.delete \n5.clear \n6.enter your choice:"))
    #         elif b==2:
    #             k=input("whose phnonenumber you want to delete?")
    #             l=pb[k]
    #             print(l)
    #             j=l['phonenumber']
    #             print(j)
    #             m=int(input("which phonenumber you want to delete?"))
    #             del j[m-1]
    #             print(pb)
    #             b=int(input("what dp you want to delete? \n1.name \n2.phonenumber \n3.email \n4.address \n5.nothing to delete \n6.select from the choice"))
    #         elif b==3:
    #             k=input("whose email you want to delete?")
    #             l=pb[k]
    #             print(l)
    #             j=l['email']
    #             print(j)
    #             m=int(input("which email you want to delete?"))
    #             del j[m-1]
    #             print(pb)
    #             a=int(input("\n1.add \n2.View \n3.Add/Update \n4.delete \n5.clear \n6.enter your choice:"))
                        




    





                        








       

         






