#Public - Everyone can see
#Protected - whom you want to see?
#Private - only you can see.

class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9
    __private = 98

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newlweaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def change_leaves(cls, newleaves):
        return cls.no_of_leaves

    @classmethod
    def change_leaves(clscls, newleaves):
        print("This is good"+ string)
emp = Employee("rudra", 6589, "Students")
#print(emp._protec)
print(emp._Employee__private)    # In the private (_class name) must be written in the print statement.




