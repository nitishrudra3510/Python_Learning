'''
ques.1:

mytuple = ("I", "Love", "India")
print(mytuple)
tuple1 = list(mytuple)
print("After converting tuple into lists:", tuple1)
tuple1[2]="Kanykuamri"
print("Afetr changing: ",tuple1)
finaltuple=tuple(tuple1)
print(finaltuple)

'''

#ques.3:
'''
list1=input("data: ")
mytuple = list1.split(",")
print(mytuple)
tuple1=tuple(mytuple)
print(tuple1)
print(len(tuple1))
'''
'''
#membership in tuples

x = (1,2,3,45,6)
print(45 in x)
'''
'''
data = input("data: ")
list1 = data.split(",")
print("list: ",list1)
tuple1=tuple(list1)
print(tuple1)
index = int(input("index: "))
size = len(tuple1)
if index < len(tuple1) and index>=(-size):
    value=(tuple1[index])
    print("element: ", value)
else:
    print("value raise error")
'''

'''
a,b,c = 1,2,3
print(a)
print(b)
print(c)

list1 = ["python", "nitish", 1, "is"]
var1, var2, var3, var4 = list1
print(var1)
print(var2)
print(list1)


'''


'''
data1 = input("data1: ")
list1 = data1.split(",")
tuple1 = tuple(list1)
print(tuple1)
value = int(input("value: "))
print("tuple ", value, "=", tuple1 * value)

data2 = input("data: ")
list2 = data2.split(",")
tuple2 = tuple(list2)
print("Concatention: ", tuple1+tuple2)

'''

data = input("data1: ")
list1 = data.split(",")
tup1 = tuple(list1)
print(tup1)
value = input("value: ")
if value in tup1:
    print("True")
else:
    print("False")


























