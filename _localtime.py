'''
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module
to get the current hour. Here is a sample program and documentation link for you:
'''
###
'''
import time
timestamp = time.strftime("%H: %M: %S: %d: %c")
print(timestamp)
timestamp = time.strftime("%H")
print(timestamp)
timestamp = time.strftime("%M")
print(timestamp)
timestamp = time.strftime("%S")
print(timestamp)

timestamp = time.strftime("%d")
print(timestamp)

timestamp = time.strftime("%c")
print(timestamp)

'''


#another method


import time
t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
#hour = int(input("Enter hour: "))
print(hour)
if(hour>=0 and hour<12):
    print("Good Morning Nitish!")
elif(hour>=12 and hour<17):
    print("Good After Noon Nitish!")
elif(hour>=17 and hour<20):
    print("Good Evening Nitish!")
else:
    print("Good Night Nitish!")



