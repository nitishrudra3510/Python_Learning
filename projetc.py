'''You have to follow certain instructions, which are as follows:

    You have to take an integer type variable, and the input of the variable will define the length of the triangle.
    You have to declare another Boolean variable.
    When the value of Boolean is 1 i.e. True, the pattern will be printed as shown above.
    But if the value of Boolean is 0 or false, then the triangle will be printed upside down.
    The output should be like this:
        '''



print("Pattern printing")
num = int(input("Enter num how many rows you want : "))
print("Enter 1 or 0")
bool_val = input("1 for True value or 0 for False : ")
if bool_val=="1":
    for i in range(0,num+1):
        print("*"*i)
if bool_val=="0":
     for i in range(num,0,-1):
         print("*"* i)

################################ or

a = int(input("please add number of line you want to print"))
b = bool(int(input("please add 0 for False and 1 for True")))
def star(a, b):
    if b == True:
        c = 1
        while c <= a:
            print(c * "*")
            c = c + 1
    else:
        while a > 0:
            print(a * "*")
            a = a - 1


star(a,b)
