# import math
# print(math.sqrt(25))
# print(math.factorial(10))
# print(math.sin(0))
# print(math.cos(0))


# import random
# print(random.random())
# print(random.randint(100,999))
# print(random.choice([1,2,3,4,5,6]))

# import datetime
# print(datetime.date.today())
# print(datetime.date.today().year)
# print(datetime.date.today().month)
# print(datetime.date.today().day)
# print(datetime.time(11,45,25))

# from datetime import datetime
# full_date=datetime.now()
# print(full_date.strftime("%y"))
# print(full_date.strftime("%Y"))
# print(full_date.strftime("%m"))
# print(full_date.strftime("%d"))
# print(full_date.strftime("%a"))
# print(full_date.strftime("%A"))
# print(full_date.strftime("%b"))
# print(full_date.strftime("%B"))
# print(full_date.strftime("%d %B %Y"))

# lambda function
# anounymous function

# lambda arguments:expression
 
# map(),filter,reduce

# def find_sum(x,y):
#     return x+y
# print(find_sum(4,5))

# f=lambda x,y:x+y
# print(f(4,5))


# l=[10,11,12,13,14,15]
# res=list(map(lambda i:i**2,l))
# print(res)

# filter()

# l=[10,11,12,13,14,15]
# result=[]
# for i in l:
#     if i%2==0:
#         result.append(i)
# print(result)

# print(list(filter(lambda i:i%2==0,l)))
# print(list(map(lambda i:i%2==0,l)))

# import functools
# l=[10,11,12,13,14,15]
# print(functools.reduce(lambda x,y:x+y,l))

# iterators, generators and decorators


# function recursion

# def greeting():
#     print("hello")
#     greeting()
# greeting()

# def find_fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*find_fact(n-1)
# n=int(input("Enter a number: "))
# print(find_fact(n))

