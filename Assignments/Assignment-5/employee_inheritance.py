class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + '@email.com'

    def full_name(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

emp1=Employee('Sushree','Mishra',20000)
print (emp1.email)

class Developer(Employee):
    raise_amt=1.10
    pass

dev1=Developer('John','Smith',5000)
dev2=Developer('Mill','Harry',6000)

print ("Email id of %s is : " %dev1.first ,dev1.email)
print ("Email id of %s is : " %dev2.first ,dev2.email)

print ("Salary of %s before increment is :" %dev1.first ,dev1.pay)
dev1.apply_raise()
print ("Salary of %s after increment is :" %dev1.first ,dev1.pay)
