# Non- Keyword arguments(*args):

#def functions_name_print(a, b, c, d):
 #   print(a, b, c, d)


def funargs(normal, *argsrohan):
    print(normal)
    print(argsrohan)
    for item in argsrohan:
        print(item)
        
#functions_name_print("Harry", "Rohan", "Skill", "Rudra")

har = ["Harry", "Rohan", "Sunil", "Rudra"]
normal = "I am a normal Arguments and the students are: "

funargs(normal, *har)


################################################################


def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    print(argsrohan)
    for item in argsrohan:
        print(item)
    print("\nNow I would like to introduce some of our heroes:")
    for key,value in kwargsbala.items():
        print(f"{key} is a {value}")
        
#functions_name_print("Harry", "Rohan", "Skill", "Rudra")

har = ["Harry", "Rohan", "Sunil", "Rudra"]
normal = "I am a normal Arguments and the students are: "
kw = {"Rohan": "Monitor", "Rudra": "Teacher", "Abhishekh": "Cook"}
funargs(normal, *har, **kw)
