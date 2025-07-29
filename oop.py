# class Student:
#     def set_student(self,name,age,place,email):
#         self.name=name
#         self.age=age
#         self.place=place
#         self.email=email
#     def studnet_info(self):
#         print(f"Name:{self.name}\nAge:{self.age}\nPlace:{self.place}\nEmail:{self.email}\n")
        
# stud1=Student()
# stud1.set_student("abc",24,"calicut","abc@gmail.com")
# stud1.studnet_info()

# stud2=Student()
# stud2.set_student("xyz",23,"kochi","xyz@gmail.com")
# stud2.studnet_info()


# class Student:
#     def __init__(self,name,age,place,email):
#         self.name=name
#         self.age=age
#         self.place=place
#         self.email=email
#     def studnet_info(self):
#         print(f"Name:{self.name}\nAge:{self.age}\nPlace:{self.place}\nEmail:{self.email}\n")
        
# stud1=Student("abc",24,"calicut","abc@gmail.com")
# stud1.set_student("abc",24,"calicut","abc@gmail.com")
# stud1.studnet_info()

# stud2=Student()
# stud2.set_student("xyz",23,"kochi","xyz@gmail.com")
# stud2.studnet_info()




# class Bank:
#     bank_name="Punjab National Bank\n---------------------"
#     def __init__(self,name,acc_no):
#         # print(Bank.bank_name,"\n")
#         self.name=name
#         self.accno=acc_no
#         self.balance=1000
        
#     def deposit(self,dep_amt):
#         print(Bank.bank_name)
#         self.depo=dep_amt
#         self.balance+=self.depo
#         print(f"Name:{self.name}\nAccount No:{self.accno}\nDeposit Succesful\nBalance={self.balance}\n")
        
#     def withdraw(self,with_amt):
#         print(Bank.bank_name)
#         self.withd=with_amt
#         if self.withd>self.balance or self.withd<=0:
#             print("Name:{self.name}\nAccount No:{self.accno}\nCannot Withdraw")
#         else:
#             self.balance-=self.withd
#             print(f"Name:{self.name}\nAccount No:{self.accno}\nWithdrawal succesful\nBalance={self.balance}\n")


# user1=Bank("Dinu","001")
# user1.deposit(5000)
# user1.withdraw(1000)






# task 

# class Ekart:
#     def __init__(self):
#         self.cart=[]
    
#     def add_product(self,name,quantity):
#         self.name=name
#         self.quantity=quantity
#         self.cart.append((self.name,self.quantity))
#         print(f"My Cart: {self.cart}")

#     # def remove_product(self,name):
#     #     self.rem_name=name
#     #     if self.rem_name in self.cart:
#     #         self.cart.pop()
#     #         print(self.cart)
    
#     def remove_product(self,name):
#         for i in self.cart:
#             if i[0]==name:
#                 self.cart.remove(i)
#                 break
#         print(f"My Cart after removing product: {self.cart}")
        
#     def total_quantity(self):
#         self.total=0
#         for i in self.cart:
#             self.total+=i[1]
#         print(f"Total Quantity in Cart: {self.total}")
        

        

# user1 = Ekart()
# user1.add_product("mobile", 1)
# user1.add_product("laptop", 2)
# user1.add_product("charger", 3)

# user1.total_quantity()

# user1.remove_product("laptop")
# user1.total_quantity()



# class Student:
#     institution="Luminar"
    
#     def __init__(self,name,place):
#         self.name=name
#         self.place=place
        
#     def student_info(self):
#         print(f"name:{self.name}\nplace:{self.place}")
        
# stud1=Student("A","calicut")
# stud2=Student("B","calicut")
# stud1.student_info()
# stud1.place="Kochi"
# print(stud1.place)
# print(stud2.place)
# print(Student.institution)
# # stud2.institution="xyz"
# # print(stud2.institution)
# Student.institution="Luminar technolab"
# print(stud1.place)
# print(stud2.place)



# types of methods
# instance method
# class method
# static method 



# class Student:
#     institution="Luminar"  #class variable
    
#     def __init__(self,name,place):
#         self.name=name      #instance variable
#         self.place=place
        
#     def student_info(self):     # instance method
#         print(f"name:{self.name}\nplace:{self.place}")

#     @classmethod
#     def change_data(cls):   # class method
#         Student.institution="Luminar technolab"
#         cls.institution="xyz"
#         print(cls.institution)
    
#     def change_stud_institution(self):
#         self.institution="xyz"
    
#     def greeting():
#         print("Hello")

# stud1=Student("A","calicut")
# # stud1.student_info()
# # Student.student_info()
# Student.change_data()
# stud1.change_data()


# Inheritence
# Single Level Inheritence
# class Parent:
#     def parent_features(self):
#         print("Parent features...")

# class Child(Parent):
#     def child_features(self):
#         print("child features...")


# p1=Parent()
# p1.parent_features()
# c1=Child()
# c1.child_features()
# c1.parent_features()


# multi level Inheritence

# class GrandParent:
#     def gparent_features(self):
#         print("grand parent features")
    
# class Parent(GrandParent):
#     def parent_features(self):
#         print("Parent features...")

# class Child(Parent):
#     def child_features(self):
#         print("child features...")
        

# c1=Child()
# c1.child_features()
# c1.parent_features()
# c1.gparent_features()


# Multiple Inheritence

# class Parent1:
#     pass
# class Parent2:
#     pass
# class Child(Parent1,Parent2):
#     pass

# Heirarchical Inheritence

# class Parent:
#     pass
# class Child1(Parent):
#     pass
# class Child2(Parent):
#     pass


# class Person:
#     def __init__(self,name,place):
#         self.name=name
#         self.place=place
    
#     def info(self):
#         print(f"{self.name},{self.place}")

# class Student(Person):
#     def __init__(self,roll_no,sub1,sub2,name,place):
#         self.rollno=roll_no
#         self.sub1=sub1
#         self.sub2=sub2
#         # super().__init__(name,place)
#         Person.__init__(self,name,place)
    
#     def student_info(self):
#         print(f"{self.name}\n{self.place}\n{self.rollno}\n{self.sub1}\n{self.sub2}")

# stud1=Student(1,35,45,"A","Calicut")
# stud1.student_info()


# from multipledispatch import dispatch

# class FindSum:
#     @dispatch(int,int,int)
#     def find_sum(self,a,b,c):
#         print(a+b+c)
    
#     @dispatch(int,int)
#     def find_sum(self,a,b):
#         print(a+b)
    
#     @dispatch(str,str)
#     def find_sum(self,a,b):
#         print(a+b)

# s=FindSum()
# s.find_sum(5,1,2)
# s.find_sum(5,1)
# s.find_sum("Good ","Morning")


# operator overloading

# print(1+2)
# print("good"+"morning")

# class A:
#     def __init__(self,num):
#         self.num=num
        
#     def __add__(self,other):
#         return self.num+other.num
    
#     def __sub__(self,other):
#         return self.num-other.num
    
#     def __mul__(self,other):
#         return self.num*other.num
    
#     def __truediv__(self,other):
#         return self.num/other.num
    
#     def __gt__(self,other):
#         if self.num>other.num:
#             return self.num
#         else:
#             return other.num
    
#     def __lt__(self,other):
#         if self.num<other.num:
#             return self.num
#         else:
#             return other.num
    
#     def __ge__(self,other):
#         if self.num>=other.num:
#             return self.num
#         else:
#             return other.num
    
#     def __le__(self,other):
#         if self.num<=other.num:
#             return self.num
#         else:
#             return other.num
    
# a1=A(10)
# a2=A(20)
# print(a1+a2)
# print(a1-a2)
# print(a1*a2)
# print(a1/a2)
# print(a1>a2)
# print(a1<a2)
# print(a1>=a2)
# print(a1<=a2)



# user defined exception 

# class ValueSmallError(Exception):
#     pass
# class ValueLargeError(Exception):
#     pass

# x=10
# while True:
#     n=int(input("Enter the Number: "))
    
#     try:
#         if n<x:
#             raise ValueSmallError
#         elif n>x:
#             raise ValueLargeError
#         else:
#             print("Correct!!")
#             break
#     except ValueSmallError:
#         print("Value Small Error")
#     except ValueLargeError:
#         print("Value Large Error")


# Access Specifiers - public, protected, private
# name - public
# _name - protected
# __name - private



# class Employee:
#     def __init__(self):
#         self.__salary=30000
    
#     def get_salary(self):
#         print(f"Salary:{self.__salary}")
#         print("=============",id(self.__salary))
        
#     def set_salary(self,amount):
#         self.__salary=amount

# emp1=Employee()
# emp1.set_salary(4000)
# emp1.get_salary()
# print(emp1.__salary)
# print(emp1._Employee__salary)
# emp1.__salary=60000
# print(emp1.__salary)
# print(id(emp1.__salary))


    # name mangling
# self.__salary
# _Employee__salary
# _Classname__variableName



# abstraction

# from abc import ABC,abstractmethod

# class Polygon(ABC):
#     @abstractmethod
#     def no_of_sides(self):
#         print("======")
        
#     def info(self):
#         print("Polygon info")

# class Triangle(Polygon):
#     def no_of_sides(self):
#         print("3 sides")

# class Rectangle(Polygon):
#     def no_of_sides(self):
#         print("4 sides")
        
# p1=Polygon()
# p1.no_of_sides()




# constructor - method used for initializing variables,
#               it executes when the object of class is created
#               __int__ 
# destructor - delete object reference 
#              __del__()

# class A:
#     def __init__(self):
#         print("constructor method")
#     def info(self):
#         print("Instance Method")
#     def __del__(self):
#         print("destructor method")
# print("creating an object for class A..")
# obj1=A()
# print("Execute Instance Method")
# obj1.info()
# print("program ended")

