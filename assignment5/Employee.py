#!/usr/bin/python

class Employees:
    rais=0.5
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    def form_email(self,email):
        self.email=email
        return  self.fname+"."+self.lname+'@'+self.email
    def apply_raise(self):
	return self.salary*Employees.rais
class Developer(Employees):
    rais=0.25
    def __init__(self,fname,lname,salary):
        Employees.__init__(self,fname,lname,salary)
    def apply_raise(self):
        return self.salary*Developer.rais

e=Employees('Ramya','Krishna',10000)
print(e.form_email('gmail.com'))
print("The amount of salary incremented:",e.apply_raise())
d=Developer('Surya','Marni',15000)
print(d.form_email('outlook.com'))
print("The amount of salry incremented :",d.apply_raise())
