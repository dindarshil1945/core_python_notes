# python functions
    # block of code which executes only when it is called

# built-in functions
    # print() len() type() int()

# lamda functions
# recursive function 

    
# user defined functions

# def function_name():         #function definition
#     block of statements 
    
# function_name()     #function call

# def function_name(parameters):
#     block of statements
    
# function_name(arguments)

# n1=1
# n2=2
# s=n1+n2
# print(s)


# docstring
# def add_sum(n1,n2):
#     '''returns the sum of 2 numbers'''
#     # n1=int(input("Enter the first num: "))
#     # n2=int(input("Enter the Second num: "))
#     s=n1+n2
#     print(s)
    
# add_sum(10,12)
# add_sum(1,2)
# add_sum(100,200)


# print(add_sum.__doc__)
# print(print.__doc__)
# print(len.__doc__)


# def find_sum(n1=0,n2=0,n3=0):
#     s=n1+n2+n3
#     print(s)

# find_sum(10,20,30)
# find_sum(10,20)
# find_sum(10)
# find_sum()


# def user_info(name,age):
#     print(f"Name:{name}\nAge:{age}")

# # user_info("abc",21)
# user_info(age=21,name="abc")   # keyword arguments


# def find_sum(*args): # arbitrary argument *args
#     print(sum(args))
# find_sum(1,2)
# find_sum(1,2,3,4,5,6)


# def user_info(**kwargs):
#     print(kwargs)
#     print(f"Name: {kwargs["name"]}\nAge: {kwargs["age"]}")

# user_info(name="abc",age=21)
# user_info(name="abc",age=21,place="calicut")


# def find_sum(*args): # arbitrary argument *args
#     return sum(args)

