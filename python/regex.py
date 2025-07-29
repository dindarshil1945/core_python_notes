# # regular expression
# import re
# password="abc@123"
# pattern="\d"
# print(re.search(pattern,password))
# print(re.findall(pattern,password))
# print(re.finditer(pattern,password))
# print(re.sub(pattern,"*",password))
# print(re.split(pattern,password))


# if re.search(pattern,password):
#     print("valid password")
# else:
#     print("invalid password")


# import re
# username=input("Enter the username: ")
# # pattern="[abc]"
# # pattern="[0-9]"
# # pattern="[0-9a-z@]"
# pattern="^abc"
# print(re.search(pattern,username))
# print(re.findall(pattern,username))
# if re.search(pattern,username):
#     print("Valid username")
# else:
#     print("Invalid username")
    
    
# metacharacters/quantifiers
# [abc]- returns a match if the string contains any of the characters within the list
# [123]-
# [0-9]
# [0-9a-z]
# [0-9a-zA-Z]
# ^p - returns a match if the string starts with "p"
# ^$ - returns a match if the string ends with "p"
# ^[abc]- 



# import re
# username=input("Enter the username: ")
# # pattern="[abc]"
# # pattern="[0-9]"
# # pattern="[0-9a-z@]"
# pattern="^[6-9][0-9]{9}$"
# print(re.search(pattern,username))
# print(re.findall(pattern,username))
# if re.search(pattern,username):
#     print("Valid username")
# else:
#     print("Invalid username")

# string1="the rain in spain is heavy"
# pattern="in*"
# pattern="in+"
# print(re.findall(pattern,string1))

# n* - zero or more occurences
# n+ - one or more occurences

# username- min 8 characters, alphabert,special,number

# a+
# a*
# a?
# (a|b)

# +91-9898989898
# +91 9898989898
# +919898989898
# 9898989898

# import re
# phone=input("Enter phone num: ")
# pattern=r"^(\+91[\s\-]?)?([6-9][0-9]{9})$"
# if re.search(pattern,phone):
#     print("valid")
# else:
#     print("invalid")

# import re

# email = input("Enter your email: ")

# # Basic email pattern
# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# if re.match(pattern, email):
#     print("Valid email address")
# else:
#     print("Invalid email address")


# import re
# username="pyton programming"
# pattern="on\Z"
# pattern=r"\d"
# pattern=r"\D"
# pattern=r"\w" # 0-9,a-z,_(word characters)
# pattern=r"\W" # 0-9,a-z,_(non-word characters)
# pattern=r"\S" # 0-9,a-z,_(non-word characters)
# print(re.findall(pattern,username))
# if re.search(pattern,username):
#     print("valid username")
# else:
#     print("invalid username")
    
# \Aabc - startswith
# on\Z - endswith
# \bp - words starts with p 
# p\b - words ends with p
# \d - digits
# \D - non-digits
# \s - space
# \S - non-space
# \w - word charcters
# \W - non-word charcters

# numbers = [1, 2, 3]
# it = iter(numbers)  # get iterator

# print(next(it))  # 1
# print(next(it))  # 2
# print(next(it))  # 3
# print(next(it))  # StopIteration


# def count():
#     yield 1
#     yield 2
#     yield 3

# c = count()
# print(next(c))  # 1
# print(next(c))  # 2
# print(next(c))  # 3


# def star_decorator(func):
#     def wrapper():
#         print("*****")       # before
#         func()
#         print("*****")       # after
#     return wrapper

# @star_decorator
# def say_hello():
#     print("Hello!")

# say_hello()



# def str_dec(func):
#     def wrapper():
#         print("*******")
#         func()
#         print("*******")
#     return wrapper
# @str_dec
# def say_hello():
#     print("hello")

# say_hello()

# num=[1,2,3]
# it=iter(num)

# print(next(it))
# print(next(it))
# print(next(it))

# def count():
#     yield 1
#     yield 2
#     yield 3
    
# c=count()
# print(next(c))
# print(next(c))
# print(next(c))

# def str_dec(func):
#     def wrapper():
#         print("******")
#         func()
#         print("******")
#     return wrapper

# @str_dec
# def say_hello():
#     print("hello")
    
# say_hello()



# def info():
#     global x
#     x=20
#     print(x)
# x=10
# info()
# print(x)


# def change_data():
#     l=[10,20,30]
#     print(l)                  #pass by value
# l=[1,2,3]
# print(id(l))
# change_data()
# print(l)

# def change_element(l):
#     l[0]=10
#     print(l)
# l=[1,2,3]                   # pass by reference
# change_element(l)
# print(l)


# print(dir(str))
# print(dir(int))

# l=[100,200,300,400,500]
# print(list(enumerate(l,1)))

# l1=[1,2,3]
# l2=["one","two","three"]
# result=[(l1[0],l2[0])]
# print(result)
# print(list(zip(l1,l2)))