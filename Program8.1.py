# OOP tutorial
# Corey Schafer

# Attributes and Methods
# Employees data
# Attributes: First name, Last name, 

# Class: A blueprint for an instance of the class
# Instance of a class: Induvidual instance of the class 
# Instance variables contains data which unique for each instance
# Class variables are the same for all instances
# Class methods are defined by the decarator @classmethod
# Class methods takes class as the first argument, by convention its "cls"
# Class methods can be used as alternative constructors
# Static methods don't pass the instance or the class as argument
# Static methods behave as normal functions, just we include them in the class
# if they have some connection with the class
# If the method doesn't use instance or class, then it should be @staticmethod
# Subclass inherits the parent class attributes and Methods
# attributes and methods are looked down to up, from subclass to parentclass
# subclass is defined by class (parentclass)
# Special methods (Magic/Dunder) are changing the default behaviour
# Property decorators: Getters, Setters and Deleters


class Employee:
    num_of_employees = 0
    raise_amount = 1.18
    def __init__(self, first, last, pay = 0):
        self.first = first # instance variable
        self.last = last
        # self.pay = pay
        # self.email = first + "." + last + "@company.com"
        Employee.num_of_employees += 1 #Runs each time when an instance is created
    @property # Getter
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)
    @property # Getter
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    @fullname.setter # Setter
    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print("Delet name!")
        self.first = None
        self.last = None


emp1 = Employee("Bruno", "Mars", 50000)

emp1.fullname = "Ace Ventura"

# emp1.first = "Jim"
print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname

print(emp1.first)
print(emp1.email)
print(emp1.fullname)
    
    
    
    
    # def apply_raise(self):
    #     self.pay = int(self.pay * self.raise_amount)
    # def __repr__(self):
    #     return "Employee({}, {}, {})".format(self.first, self.last, self.pay)
    # def __str__(self):
    #     return "{} - {}".format(self.fullname(), self.email)
    # def __add__(self, other):
    #     return self.pay + other.pay
    # def __len__(self):
    #     return len(self.fullname())

# emp1 = Employee("Bruno", "Mars", 50000)
# emp2 = Employee("Debie", "Gibson", 70000)

# print(emp1.first)
# print(emp1.email)
# print(emp1.fullname())


# print(len(emp1))

# print(len("test"))
# print("test".__len__())

# print(emp1 + emp2)


# print(emp1)
# print(repr(emp1))
# print(str(emp1))

# print(emp1.__repr__())
# print(emp1.__str__())

# print(int.__add__(1, 2))
# print(str.__add__("a", "b"))

    # @classmethod
    # def set_arise_amount(cls, amount):
    #     cls.raise_amount = amount

    # @classmethod
    # def from_string(cls, employee_string):
    #     first, last, pay = employee_string.split("-")
    #     return cls(first, last, pay)
    
    # @staticmethod
    # def is_workday(day):
    #     if day.weekday() in range(6, 7):
    #         return False
    #     return True

# class Developer(Employee): # Sub class, inhertited from Employee class.
#     raise_amount = 1.2
#     def __init__(self, first, last, pay, prog_lang):
#         # super().__init__(first, last, pay) # Let the parent class handle these arguments
#         Employee.__init__(self, first, last, pay) # This is used when multiple inheritance exist
#         self.prog_lang = prog_lang

# class Manager(Employee):
#     def __init__(self, first, last, pay, list_of_reporting=None):
#         Employee.__init__(self, first, last, pay)
#         if list_of_reporting is None:
#             self.list_of_reporting = []
#         else:
#             self.list_of_reporting = list_of_reporting
#     def add_reporting(self, emp):
#         if emp not in self.list_of_reporting:
#             self.list_of_reporting.append(emp)        
#     def rem_reporting(self, emp):
#         if emp in self.list_of_reporting:
#             self.list_of_reporting.remove(emp)
#     def print_employees(self):
#         for emp in self.list_of_reporting:
#             print("-->", emp.fullname())


# dev_1 = Developer("John", "Doe", 30000, "C#")
# dev_2 = Developer("James", "Day", 40000, "Python")

# mgr_1 = Manager("Judit", "Manman", 90000, [dev_1])
# mgr_1.add_reporting(dev_2)
# mgr_1.print_employees()

# print(isinstance(mgr_1, Manager)) # Checks if an instance is part of a Class
# print(issubclass(Developer, Employee)) # Chaks if a subclass memebr of a parent class

#print(dev_1.fullname(), dev_1.prog_lang)
# print(help(Developer)) # Provides information about the class

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# import datetime


# my_date = datetime.date(2018, 1, 29)
# print(Employee.is_workday(my_date))

# emp_str_1 = "John-Doe-70000"
# emp_str_2 = "Steve-Smith-60000"
# emp_str_3 = "Jane-Doe-40000"

# # first, last, pay = emp_str_1.split("-")
# new_emp1 = Employee.from_string(emp_str_1) # Calling the alternative constructor to create an instance
# # new_emp1 = Employee(first, last, pay)

# print(new_emp1.fullname())
# print(new_emp1.email)


# Employee.set_arise_amount(1.12)

# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(Employee.raise_amount)


# print(Employee.num_of_employees) #Shows 2, since 2 instances were created

# print("{} {}".format(emp1.fullname(), emp1.pay))
# emp1.apply_raise()
# print("{} {}".format(emp1.fullname(), emp1.pay))
# print(emp1.__dict__) # prints the name space of the instance


# print(emp1)
# print(emp2)

# emp1.first = "Bruno"
# emp2.last = "Mars"
# emp1.email = "bruno.mars@company.com"
# emp1.pay = 50000

# emp2.first = "Debbie"
# emp2.last = "Gibson"
# emp2.email = "debbie.gibson@company.com"
# emp2.pay = 70000

# print(emp1.email)
# print(emp2.email)
# print("{} {}".format(emp1.first, emp1.last))
# print("{} {}".format(emp2.first, emp2.last))
# print(Employee.fullname(emp1)) # Calling the method from the Class, passing instance
# print(emp1.fullname()) # Calling the method by the instance
