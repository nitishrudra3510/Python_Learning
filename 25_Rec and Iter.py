#Iterative Method:

# n!= n* n-1 * n-2 * n-3................1
# n! = n * (n-1)!

def factorial_iterative(n):
    """
    :param n: Integer
    :return: n* n-1 * n-2 * n-3.....1
    
    """
    
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
number = int(input("Enter the number: "))
print("Factorial using the Iterative Method: ", factorial_iterative(number))
# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 * factorial_recursive(2)
# 5 * 4 * 3 * 2 factorial_recursive(1)
# 5*4*3*2*1 = 120

##################################################

# Factorial Recursive():

def factorial_recursive(n):
    """
    :param n: Integer
    :return: n* n-1 * n-2 * n-3.....1
    
    """
    
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    
number = int(input("Enter the number: "))
#


#print("Factorial using the iterative Method: ", factorial_iterative(number))
print("Factorial using the recursive Method: ", factorial_recursive(number))





############################################
# fibonacci series number- 0 1 1 2 3 5 8 13 21 34 55 89 144 233
# Fibonacci series:     
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
number = int(input("Enter the number: "))
print(fibonacci(number))




