#SET - Mutable
# a={1,2,3,4,5}
# print(type(a))
# print(len(a))

#how to create empty set
# c=set()
# print(type(c))

#empty curly bracket is of type dictionary
# b={}
# print(type(b))

# a={"p","q","r","s"}
# print(a)
# b={6,0,1,2,3,4,5}
# print(b)
# c={0,1,2,'p','q','r',True,False}
# print(c)
# d={1,2,3,4,1,2,3,4}
# print(d)

# e={2,3,'a',True,1,'hai'}
# a={'hai','abc','AB',8,6}
# for i in e:
#     print(i)

# s={1,2,3}
# # s.remove(4)
# # s.discard(4)
# print(s)
# add, update, remove, discard,clear, pop,delete
# e.add(5)
# print(e)
# k=[10,20,30]
# e.update(k)  
# print(e)
# can update another set, string or list by this method
# print(e)
# e.remove(9)
# print(e)
# e.discard(7)
# print(e)
# e={"p",2,True,"K"}
# e.clear()
# print(e)
# print(type(e))
# u=e.pop()
# print(u)
# print(u,"is the popped value")
# print(e)
# del e
# print(e)

#Methods union, intersection, symmetric difference, difference, 
# a={1,2,3,4,5,6}
# b={5,6,7,8,9,10}
# x=a.union(b)
# print(x)
# print(a|b)
# x=a.intersection(b)
# print(x)
# print(a&b)
# x=a.symmetric_difference (b)
# print(x)
# print(a^b)
# x=a.difference(b)
# print(x)
# print(a-b)
# y=b.difference(a)
# print(y)
# # print(b-a)

# a={1,2,3,4,5,6,7,8,9,10} 
# # # odd and even are subset of a , a is superset of odd and even
# odd={1,3,5,7,9}
# even={2,4,6,8,10} 
# print(odd.isdisjoint(even)) 
# # true, as there is no intersection in subset odd and even
# print(odd.isdisjoint(a)) 
# # false
# print(a.isdisjoint(even))
#  # false

# print(odd.issubset(a))
# print(even.issubset(odd))
# print(a.issuperset(even))
# print(even.issuperset(odd))

# a={1,2,3,4,5,6,7,8,9,10}
# odd = {1,3,5,7,9}
# even={2,4,6,8,10}
# X=a.

#Dictionary

# a={"name":"anjali","age":"26", "place":"TVM"}
# b={"name":"sneha","age":20,"course":"python"}
# print(b["name"])
# print(b.get("course"))
# print(a["name"])
# print(a["age"])
# print(a["place"])
# print(a.get("place"))
# print(len(a))
# a["course"]="java"
# a["name"]="ammu"
# print(a)
#assigning new value for key
# a['place'] = 'kochi'
# print(a)
# a['age'] = '12'
# a['name']='vishnu'
# print(a)
#key,value,item

# print(a.keys())
# print(a.values())
# print(a.items()) 
# # in a list- get key and value as tuples

a={"name":"anjali","age":"26", "place":"TVM"}
# print(('name' in a)) 
# # print('ammu' in a)    False
print('cochi' in a.values())  
# a["course"] = "python"
# print(a)
# # methods - update

a.update({'name':'sneha'})
print(a)
# a.update({'game':'hockey'})
# print(a)
