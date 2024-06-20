#map function: function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
number = ["3", "34", "65"]
number = list(map(int, number))
for i in range(len(number)):
    number[i] = int(number[i])
    

number[2] = number[2] + 1
print(number[2])

'''
def sq(a):
    return a*a

num = [2,3,4,5,6,7,8,9]
square = list(map(sq, num))
print(square)
'''



num = [2,3,4,5,6,7,8,9]
square = list(map(lambda x: x*x, num))
print(square)



###############################################

def square(a):
    return a*a
def cube(a):
    return a*a*a

func = [square, cube]
#num = [1,2,3,4,5,6]
for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)


#################################################
#============Filter function========================:
#The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
list_1 = [1,2,3,4,5,6]
def is_greater_5(num):
    return num>5
greater_than_5 = list(filter(is_greater_5, list_1))
print(greater_than_5)

###############
def fun(variable):
    letters = ["a", "e", "i", "o", "u"]
    if (variable in letters):
        return True
    else:
        return False
# sequence
sequence = ["g", "e", "e", "j", "k", "p", "r"]
#using filter fun
filtered = filter(fun, sequence)

print("The filtered letters are:")
for s in filtered:
    print(s)


##============================Reduce===========================
from functools import reduce
list1 = [1,2,3,4,5]
num = reduce(lambda x,y:x+y, list1)
#num = reduce(lambda x,y:x*y, list1)

#num = 0
#for i in list1:
#    num = num + i
print(num)


