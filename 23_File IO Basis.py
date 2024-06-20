# File to basics.
'''
"r" - open file for reading - default mode
"w" -open a file for writing
"x" -creates file if not exists.
"a" - And more content to a file.
"t" - text mode - default mode
"b" - binary mode
"+" - read and write

'''

f = open("python.txt")
content = f.read()
print(content)

f.close()


#################

f = open("python.txt", "rt")
content = f.read(5)
print(content)

content = f.read(5)
print(content)
f.close()

#############

f = open("python.txt", "rt")
content = f.read(555)
print("1", content)

content = f.read(5555)
print("2", content)
f.close()


#######################  print new line character n each word
f = open("python.txt", "rt")
content = f.read()
for line in content:
    print(line)

f.close()



########## read each line


f = open("python.txt", "rt")
# content = f.read()
for line in f:
    print(line, end="")

f.close()


#########################

print("\n")
f = open("python.txt", "rt")
#print(f.readline())
#print(f.readline())
print(f.readlines()) # changes in lists in one line
# 
# 
# content = f.read()


f.close()


################################################################

f = open("python.txt", "w")
f.write("Nitish kumar is aab boy")
f.close()


########  append mode: a:  open an existing file for append operation. It won’t override existing data.

f = open("python.txt", "a")
f.write("Nitish kumar is aab boy\n")
f.close()


######################################
#w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well

f = open("python.txt", "w")
a = f.write("Nitish kumar is aab boy")
print(a)
f.close()

################  r+:  To read and write data into the file. The previous data in the file will be overridden.

f = open("python.txt", "r+")

print(f.read())
f.write("Thank you")



f.close()













