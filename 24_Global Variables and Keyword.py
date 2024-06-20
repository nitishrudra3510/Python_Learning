# global variables:

l = 10 # Global value
def functional(n):
    l = 5 #local  -- print 5 not 10 because l is inside tge fumctioms
    m = 8 #local
    print(l, m)
    print(n, "I have printed")


functional("This is me")
#print(m)   - beacuse m is defined in local not global varibles
print(l)


#####################################


#global keyboard

l = 10 # Global value
def functional(n):
    #l = 5 #local
    global l # global keyword
    l = l + 45 # global variables can changed from local variables but can not change from global variales
    
    m = 8 #local
    print(l, m)
    print(n, "I have printed")


functional("This is me")
#print(m)   - beacuse m is defined in local not global varibles
print(l)




def rudra():
    x = 20
    def rohan():
        global x
        x = 88
    print("before calling rohan():", x)
    rohan()
    print("ater calling rohan():", x)
rudra()




























