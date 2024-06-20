**Notes - Python Literals:**

**I. String Literals:**
- Data given in a variable or constant.
- Formed by enclosing text in quotes (single or double).
- Two types: Single-line and Multi-line strings.
  - Single-line: Terminated within a single line.
    - Example: `text1 = 'hello'`
  - Multi-line: Written in multiple lines.
    - Created using backslashes at the end of each line or triple quotation marks.


II. Numeric literals:
Numeric Literals are immutable. Numeric literals can belong to following four different numerical types.

Int(signed integers)	                                              Long(long integers)	          float(floating point)	                     Complex(complex)
Numbers( can be both positive and negative) with 	     Integers of unlimited size followed 	     Real numbers with both integer 	  In the form of a+bj where a forms the real part and 
no fractional part.eg: 100                            by lowercase or uppercase L eg: 87032845L     and fractional part eg: -26.2            b forms the imaginary part of the complex number. eg: 3.14j

x = 0b10100 #Binary Literals  
y = 100 #Decimal Literal   
z = 0o215 #Octal Literal  
u = 0x12d #Hexadecimal Literal  
  
#Float Literal  
float_1 = 100.5   
float_2 = 1.5e2  
  
#Complex Literal   
a = 5+3.14j  
  
print(x, y, z, u)  
print(float_1, float_2)  
print(a, a.imag, a.real)  


**III. Boolean Literals:**
- Values: True or False.
- Example:
  - `x = (1 == True)`
  - `y = (2 == False)`
  - `a = True + 10`
  - Output: "x is True", "y is False", "a: 11"

**IV. Special Literals:**
- Special literal: None.
- Used to represent a field not created or end of a list.

**V. Literal Collections:**
- Types: List, Tuple, Dict, Set Literals.
- List: Mutable, values separated by commas and enclosed within square brackets.
- Dictionary: Key-value pairs, enclosed in curly braces.
- Tuple: Immutable collection of different data types.
- Set: Unordered dataset, enclosed in curly braces.

**Examples:**
- List Literals: `list = ['John', 678, 20.4, 'Peter']`
- Dictionary Literals: `dict = {'name': 'Peter', 'Age': 18}`
- Tuple Literals: `tup = (10, 20, "Dev", [2, 3, 4])`
- Set Literals: `set = {'apple', 'grapes', 'guava', 'papaya'}`

These are the Python literals along with examples and explanations.
