**Python Comments**

**Introduction:**
- Comments in Python are used to describe the code, provide explanations, and make the program more understandable.
- Python interpreter ignores comments while interpreting the script during program execution.
- There are three main types of comments in Python: single-line comments, multi-line comments, and documentation strings.

**Advantages of Using Comments:**
- Improve code comprehensibility.
- Remember why specific sections of code were created.
- Control code execution.
- Provide an overview of the program or project metadata.
- Add notes, resources, or explanations to the code.

**Types of Comments in Python:**

1. **Single-Line Comments:**
   - Quick descriptions for parameters, function definitions, and expressions.
   - Marked by a hashtag `#` at the beginning and extends until the end of the line.
   - Can span multiple lines by adding `#` to subsequent lines.
   
   **Example:**

   # This code is to show an example of a single-line comment
   print('This statement does not have a hashtag before it')
   

2. **Multi-Line Comments:**
   - Python does not have a built-in syntax for multi-line comments, but there are workarounds:
     - Using multiple `#` for each line.
#    - Using string literals within triple quotes `"""` as a multi-line comment.
     
   **Examples:** Using multiple `#`:

   # it is a
   # comment
   # extending to multiple lines


   Using string literals within triple quotes:
   'it is a comment extending to multiple lines'

3. **Python Docstring:**
   - Enclosed in triple quotes immediately after the function, module, or class definition.
   - Used to document Python modules, methods, classes, and functions.
   - Accessible using the `__doc__` attribute.

   **Example:**
   def add(x, y):
      """This function adds the values of x and y"""
      return x + y

   # Displaying the docstring of the add function
   print(add.__doc__)

In summary, comments in Python play a crucial role in documenting code, making it more readable, and providing explanations for various elements of the program. Understanding the different types of comments and how to effectively use them can greatly enhance the clarity and maintainability of your code.
