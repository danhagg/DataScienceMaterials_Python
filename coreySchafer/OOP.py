class Employee:

    raise_amount = 1.04  # class variables
    num_of_emps = 0  # will increment by one in __init__ method

    def __init__(
            self, first, last, pay
    ):  # initalize class attributes - the 'initialized' or 'constructor'
        # set all instance variables (below) within init method
        self.first = first  # these are 'attributes' of class 'Employee'
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1

    # we dont want it as a method we want to keep as attribute so we add "@property decorator"
    @property  # add property decorator makes it an attr
    def email(
            self
    ):  # in creating methods in a class: receive instance (self) as 1st arg
        return '{}.{}@email.com'.format(self.first, self.last)

    @property  # add property decorator makes it an attribute
    def fullname(self):  # needs 'self' argument for instance
        return '{} {}'.format(self.first, self.last)

    @fullname.setter  # allows you to set the fullname property called "name" in parameters
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter  # allows you to set the fullname property called "name" in parameters
    def fullname(self):
        print('Name deleted')
        self.first = None
        self.last = None

    def apply_raise(
            self
    ):  # class method Regular methods take instance 'self' as first argument
        # by using self.raise_amount allows any subclass (instance)
        # to override, see below when we change emp_1.raise_amount
        self.pay = int(self.pay * self.raise_amount)
        # can use
        # self.pay = int(self.pay * Employee.raise_amount)

    @classmethod  # add @classmethod decorator to a regular method
    def set_raise_amt(
            cls, amount
    ):  # automatically take class as first argument, cls used as var name
        cls.raise_amt = amount

    @classmethod  # Class methods can also be used as alternative constructors. "from_string" constructor
    def from_string(cls, emp_str):  # 'from' convention
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # return new employee object

    @staticmethod  # static methods dont pass instance or class variables
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(
            self
    ):  # Dunder methods let you emulate the behavior of built-in types for classes.
        return "Employee('{},{},{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    # Compute total wage bill by explicitly dunder-adding salaries
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)


# create Employee objects/instances Employee() will trigger __init__ method and "emp_1" passed in as "self"
emp_1 = Employee('Keyzer', 'Soze',
                 50000)  # instance "self" passed automatically
emp_2 = Employee('Test', 'User', 60000)

emp_5_str = 'Colin-Jackson-100000'
new_emp = Employee.from_string(emp_5_str)  # use from_string class method
print("Generated from class method constructor is " + new_emp.email)

import datetime
my_date = datetime.date(2016, 7, 11)  # a monday
print(Employee.is_workday(my_date))

print("__repr__ method now allows 'print(repr(emp_1)) = '",
      repr(emp_1))  # the repr functionality has changed to __repr__
print("__str__ method now allows 'print(str(emp_1)) = '",
      str(emp_1))  # the str functionality has changed to __str__
print("__len__ method now allows 'print(len(emp_1)) = '",
      len(emp_1))  # only works with __len__ method defined above
print("__add__ method now allows 'print(emp_1 + emp_2) = '",
      emp_1 + emp_2)  # only works with __add__ wage calc method defined above
emp5 = Employee('John', 'Smith', 50000)
emp5.fullname = "Dan Haggerty"
# print the namespace of emp5
print(emp5.__dict__)
del (emp5.fullname)


# new subclass
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


# new subclass
class Manager(Employee):

    # never pass mutable empty lists/dicts as default arg, use None
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname)

            # 'method resolution order' looks for __init__ in Developer then Employee


dev_1 = Developer('Englebert', 'Humperdink', 50000, 'Python')
dev_2 = Developer('Barry', 'Manilow', 30000, 'Rust')

mgr_1 = Manager('Bobby', 'Davro', 90000, [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.print_emps()

print()
# isinstance will tell us if object is instance of a class
print('Is mgr_1 an instance of Manager? ' + str(isinstance(mgr_1, Manager)))
print('Is mgr_1 an instance of Employee? ' + str(isinstance(mgr_1, Employee)))
print('Is mgr_1 an instance of Developer? ' +
      str(isinstance(mgr_1, Developer)))
print()
# issubclass will tell us if object is instance of a class
print('Is Developer a subclass of Employee? ' +
      str(issubclass(Developer, Employee)))
print('Is Manager an subclass of Employee? ' +
      str(issubclass(Manager, Employee)))

print('Is Manager an subclass of Developer? ' +
      str(issubclass(Manager, Developer)))
