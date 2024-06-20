'''
What is Anonymous function?

In Python programming, an anonymous function or lambda expression is a function definition that is not bound to an 
identifier (def).

The anonymous function is an inline function. The anonymous functions are created using a lambda operator
and cannot contain multiple expressions.

The following example will show how anonymous functions work:

result = lambda n1, n2, n3: n1 + n2 + n3;
print ("Sum of three values : ", result( 10, 20, 25 ))

In the above code, we have created an anonymous function that adds three numbers. The function is 
stored in a variable named result. The function can then be called using this variable.
In the above code, the function has been called with three different parameter values for the function call.

Anonymous functions can accept inputs and return the outputs, just like other functions do.
Why do we use Python Lambda Functions?

The main objective of anonymous functions is that, when we need a function just once, anonymous functions come in handy.
Lambda operator is not only used to create anonymous functions, but there are many other uses of the lambda expression.
We can create anonymous functions wherever they are needed. Due to this reason, Python Lambda Functions
are also called as throw-away functions which are used along with other predefined functions such as reduce(), 
filter(), and map().

These functions help reduce the number of lines of the code when compared to named Python functions.
Significant Differences Between Lambda Expressions And Simple Functions.

    Can be passed immediately with or without variables.
    They are inline functions.
    Automatic return of results.
    There is neither a document string nor a name.

Python List sort():

Sorting means arranging data systematically. If the data we want to work with is not sorted, we will face problems
finding the desired element.

The Python language, like other programming languages, can sort data.

Python has an in-built method i.e. sort(), which is used to sort the elements of the given list in a specified ascending
or descending order. There is also a built-in function i.e. sorted(), that builds a new sorted list from an iterable
like list, dictionary, etc.

The syntax of the sort() method is:

list.sort(key=myFunc ,reverse=True|False)

Parameter Values:-

Parameters

Values

#key:

In the key parameter, we specify a function that is called on each list element before making comparisons. 


#reverse:
	

This is optional. False will sort the list in ascending order, and true will sort the list in descending order.


Default is reverse=False.


Sort() does not return any value, but it changes from the original list.


'''

# Lambda functions or anonymous functions
# def add(a, b):
#     return a+b
#
# # minus = lambda x, y: x-y
#
# def minus(x, y):
#     return x-y
#
# print(minus(9, 4))
'''
def a_first(a):
    return a[1]
a = [[1, 14], [5,6], [8, 14]]
a,sort(key=a_first)
print(a)
'''

a =[[1, 14], [5, 6], [8,23]]
a.sort(key=lambda x:x[1])
print(a)
  
