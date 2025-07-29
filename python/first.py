# print("Hello World")
# age=int(input("Enter your Age: "))

# if age>=18:
#     print("Can Vote")
# else:
#     print("Cannot Vote")

# print("BYE")

# num1=int(input("Enter a Number: "))
# num2=int(input("Enter another Number: "))
# sum=num1+num2
# print(f"Sum of {num1} and {num2} is {sum}")


# 24-6-2025

# for i in range(1,5):
#     print("*",end=" ")
# print()
# for i in range(1,5):
#     print("*",end=" ")
# print()
# for i in range(1,5):
#     print("*",end=" ")
# print()
# for i in range(1,5):
#     print("*",end=" ")
# print()

# for j in range(5):
#     for i in range(5):
#         print("*",end=" ")
#     print()

# for j in range(5):
#     for i in range(5):
#         print(i,end=" ")
#     print()

# for j in range(1,6):
#     for i in range(1,6):
#         print(i,end=" ")
#     print()

# for j in range(5):
#     for i in range(5):
#         print(i+1,end=" ")
#     print()
    
# for j in range(5):
#     for i in range(5):
#         print(j,end=" ")
#     print()

# a=int(input("Enter a Number: "))

# for i in range(1,11):
#     product=i*a
#     print(f"{i} * {a} = {product}")


# for i in range(1,101):
#     if i%2==0:
#         print(i)


# sum=0
# for i in range(1,101):
#     sum=sum+i             #s+=i
# print(sum)



# a=int(input("enter a number: "))
# fact=1

# for i in range(1,a+1):
#     fact*=i
# print(fact)



# num=int(input("Enter a Number: "))
# count=0
# while num>0:
#     rem=num%10
#     count+=1
#     num=num//10
# print(count)

# num=int(input("Enter a Number: "))
# temp=num
# rev=0
# while num>0:
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)
# if rev==temp:
#     print("palindrome")
# else:
#     print("Not Palindrome")





# 25 june 2025


# a=int(input("Enter Number of Rows: "))
# for rows in range(a+1):
#     for cols in range(rows):
#         print("*",end=" ")
#     print()


# for rows in range(5,0,-1):
#     for cols in range(rows,0,-1):
#         print("*",end=" ")
#     print()
    
    
# for rows in range(6):
#     for cols in range(5-rows):
#         print("*",end=" ")
#     print()

# for rows in range(5):
#     for cols in range(5-rows):
#         print(" ",end=" ")
#     for cols in range(rows+1):
#         print("*",end=" ")
#     print()


# for i in range(5):
#     if i==0 or i==5-1:
#         for j in range(5):
#             print("*",end=" ")
#         print()
#     else:
#         for j in range(1):
#             print("*",end=" ")
#         for j in range(1,4):
#             print(" ",end=" ")
#         for j in range(5,4,-1):
#             print("*",end=" ")
#         print()
            
            
# size = 5
# for i in range(size):
#     for j in range(size):
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    
# size = 5
# for i in range(size):
#     for j in range(size):
#         if i == size - 1 or j == 0:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# size = 5
# for i in range(size):
#     for j in range(size):
#         if (i==0 or i==size-1) and (j==0 or j==size-1):
#             print(" ", end=" ")
#         elif i==0 or i==size-1 or j==0 or j==size-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# for i in range(5):
#     for j in range(5):
#         if (i==0 and (j==1 or j==2 or j==3)) or (i==1 and (j==0 or j==4)) or (i==2) or (i==3 and (j==0 or j==4)) or (i==4 and (j==0 or j==4)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# size = 5
# for i in range(size):
#     for j in range(size):
#         if i == 0 or i == size - 1 or j == 0 or j == size - 1:
#             print("*", end=" ")
#         elif (i==0 and j==4) or (i==4 and j==4):
#             print(" ", end=" ")
#         else:
#             print(" ",end=" ")
#     print()



# for i in range(5):
#     for j in range(5):
#         if j == 0: 
#             print("*", end=" ")
#         elif (i == 0 or i == 5-1) and j < 5-1:
#             print("*", end=" ")
#         elif j == 5-1 and i != 0 and i != 5-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# 26/06/2025


# numbers=[10,11,12,13,14,15]
# for i in numbers:
#     if i%2==0:
#         print(i)

# numbers=[10,11,12,13,14,15]
# for i in numbers:
#     res=i**2
#     print(res)


# numbers=[10,11,12,13,14,15]
# sum=0
# for i in numbers:
#     sum=sum+i
# print(sum)

# numbers=[13,10,11,12,14,15]
# largest=0
# for i in numbers:
#     if i>largest:
#         largest=i
# print(largest)


# numbers=[13,10,11,12,14,15]
# smallest=numbers[0]
# for i in numbers:
#     if i<smallest:
#         smallest=i
# print(smallest)

    
# numbers=[11,15,14,16,20]
# for i in numbers:
#     if i%5==0:
#         break
#     else:
#         print(i)


# numbers=[11,15,14,16,20]
# for i in numbers:
#     if i%5==0:
#         continue
#     else:
#         print(i)


# number=100
# while True:
#     num=int(input("Guess the number: "))
#     if num>number:
#         print("The number entered is higher than the actual number.")
#     elif num<number:
#         print("The number entered is shorter than the actual number.")
#     else:
#         print("Its the correct Number.")
#         break


# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15



# num = 1
# for rows in range(1, 6):
#     for cols in range(rows):
#         print(num, end=" ")
#         num += 1
#     print()


# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

# for rows in range(5,0,-1):         
#     for cols in range(5,5-rows,-1):
#         print(cols, end=" ")
#     print()




# 27/06/2025

# s="Good Morning"

# print(s)
# print(s[0])
# print(s[-1])

# range(start,end,step)
# print(s[0:4:1])
# print(s[5:12:1])
# print(s[::])
# print(s[0:])
# print(s[:])
# print(s[::-1])
# print(len(s))
# print(s[::2])
# s[0]="x"         #cannot assign as it is a str data type



# String Methods

# s="good morning"
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.capitalize())
# print(s.isupper())
# print(s.islower())
# print(s.strip())      #to remove spaces in beginng and ending of a string
# print(s.lstrip())      #to remove spaces in beginng of a string
# print(s.rstrip())      #to remove spaces in ending of a string
# print(s.split())     #split with spaces
# print(s.split("m"))     #split with spaces excluding M


# s="GOOD MORNING"
# print(s.replace("MORNING","EVENING"))
# print(s.replace("G","*"))
# print(s.replace("G","*",1)) #REPLACE ONLY ONE G THAT IS THE G THAT COMES FIRST


# print(s.ljust(10,"*"))
# print(s.rjust(10,"*"))
# print(s.center(10,"*"))

# print(s.startswith("GO"))
# print(s.endswith("ING"))


# s="123"

# print(s.isnumeric())
# print(s.isalpha())
# print(s.isalnum())
# print(s.isspace())

# s="abc @123"

# alphabets=0
# numbers=0
# spaces=0
# special=0

# for i in s:
#     if i.isalpha():
#         alphabets+=1
#     elif i.isnumeric():
#         numbers+=1
#     elif i.isspace():
#         spaces+=1
#     else:
#         special+=1
        
# print(f"Alphabets: {alphabets}")
# print(f"Numbers: {numbers}")
# print(f"Spaces: {spaces}")
# print(f"Spcl Char: {special}")


# 30/06/2025


# s="python programming"
# print(s.index("p"))
# print(s.index("y"))
# # print(s.index("x"))
# print(s.find("p"))
# print(s.find("python"))
# print(s.find("x"))
# print(s.rfind("p"))
# print(s.count("p"))
# del s
# print(s)

# s="python programming"
# print(s[0]+s[1:].replace("p","*"))



# s = input("Enter a word: ")
# if len(s)>=3:
#     if s.endswith("ing"):
#         res=s+"ly"
#     else:
#         res=s+"ing"
# else:
#     res=s
# print(res)


# item=input("Enter the Item: ")
# price=float(input("Enter the price: $"))
# ovrnight_dlvry=int(input("Overnight Delivery (0=NO/1=YES): "))
# shipping=0

# if price>=10:
#     shipping=3
# else:
#     shipping=2
    
# if ovrnight_dlvry==1:
#     shipping=shipping+5
    
# total=price+shipping

# print("Invoice")
# print(f"{item} : ${price:.2f}")
# print(f"Shipping : ${shipping:.2f}")
# print(f"Total : ${total:.2f}")




# numbers=[100,101,102,103,"python programming"]
# print(numbers[0])
# print(numbers[1:3])
# print(numbers[-1])
# print(numbers[-1][0:6])

# numbers[0]=1000
# print(numbers)



# list methods
# append(),extend()insert()


# numbers=[10,20,30,40,50]
# numbers.append(60)
# print(numbers)
# numbers.append("Python")
# numbers.append([1,2,3])
# numbers.extend([1,2,3])
# numbers.insert(2,30)
# print(numbers)

# list=[10,11,12,13,14,15,16,17]
# even=[]
# odd=[]

# for i in list:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(even)
# print(odd)




# 01/07/2025


# l=[10,11,12,13,14,15,16,17,"python"]
# pop()
# l.pop()
# l.pop(-1)
# print(l)

# l.remove("python")
# l.remove(10)
# del l[1]
# print(l)

        
        
        
# n = int(input("Enter Number to be removed: "))
# l = [10, 20, 30, 40, 50]

# if n in l:
#     l.remove(n)
#     print(f"Removed {n} from list")
# else:
#     print(f"{n} not present in list")

# print("Updated list:", l)




# l = [10, 20, 30, 10, 30, 40, 50]
# res = []

# for i in l:
#     if i not in res:
#         res.append(i)

# print(res)


# numbers=[1,2,3,4,5]
# # res=[(1,1),(2,4),(3,9),(4,16),(5,25)]
# res=[]

# for i in numbers:
#     temp=(i,i**2)                   #res.append((i,i**2))
#     res.append(temp)

# print(res)




# List Comprehension

# new_list=[expression  for item in iterable  if condition]

# result=[i for i in range(1,11)]
# print(result)

# even=[i for i in range(1,11) if i%2==0]
# print(even)

# square = [i**2 for i in range(1, 11)]
# print(square)

# number=[(i,i**2) for i in range(1,6)]
# print(number)

# new_list=[expression1  if condition1 else expression2 for item in iterable]
# new_list=[expression1  if condition1 expression2 if condition2 else expression3 for item in iterable]

# numbers=[(i,i**2) if i%2==0 else (i,i**3)for i in range(1,11)]
# print(numbers)

# s="hello"
# print(s[::-1])

# l=[10,200,300,40,50]
# print(l[::-1])
# l.reverse()
# print(l)
# l.sort()
# l.sort(reverse=True)
# print(l)

# l1=[10,20,30,40,50]
# l2=l1.copy()
# l1[0]=100
# print(l1)
# print(l2)

# a=10
# b=20
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

# a=10
# b=20

# n = int(input("Enter number of terms: "))
# a = 0
# b = 1
# count = 0

# print("Fibonacci series for", n, "terms:")
# while count < n:
#     print(a)
#     temp = a
#     a = b
#     b = temp + b
#     count += 1


# 02/07/2025


# limit = int(input("Enter the limit: "))

# print("Prime numbers up to", limit, "are:")

# for num in range(2, limit + 1):
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)


# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")


# n=int(input("Enter num: "))
# prime=True

# if n<=1:
#     print("Not Prime")
    
# if n>1:
#     for i in range(2,n):
#         if n%i==0:
#             prime=False
#             break
    
#     if prime:
#         print("It is prime")
#     else:
#         print("Not Prime")




# start= int(input("Enter starting limit: "))
# limit = int(input("Enter ending limit: "))

# for i in range(start, limit + 1):
#     prime = True

#     for j in range(2, i):
#         if i % j == 0:
#             prime = False
#             break

#     if prime:
#         print(i)



# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# count = len(str(num))

# while temp > 0:
#     digit = temp % 10
#     sum=sum+digit**count
#     temp=temp//10

# if sum == num:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")


# dictionary- mutable
# keys- immutable
# values- any data type
# dict={key:value}
# dict1={}
# dict2=dict1()

# student={"name":"abc","place":"calicut","age":23}
# print(len(student))
# print(student)
# print(student["name"])
# print(student["place"])
# student["place"]="kozhikode"
# student["email"]="dkv@123"
# print(student)


# 03/07-2025


# student={"name":"abc","place":"calicut","age":23}

# print(student["name"])
# print(student.get("name"))
# print(student.values())
# print(student.keys())
# print(student.items())

# student["email"]="abc@gmail.com"
# # update()
# student.update({"phone":1234567890})
# student.update({"place":"kozhikode"})
# print(student)

# student.pop("place")
# student.popitem()
# print(student)

# student.clear()
# print(student)

# del student



# d = {}
# for i in range(1, 6):
#     k=input("inut key:")
#     n = input("Insert value: ")
#     d[k]=n 
# print(d)



# keys=[1,2,3,4,5]
# values=["one","two","three","four","five"]
# d={}
# for i in range(len(keys)):
#     d[keys[i]]=values[i]
# print(d)

# output needed
# d={'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five'} 


# list1=[10,20,30,10,30,40,20,30]
# # d={10:2,20:2,30:3,40:1}
# d={}

# list1 = [10, 20, 30, 10, 30, 40, 20, 30]
# d = {}

# for i in list1:
#     if i in d:
#         d[i]+=1
#     else:
#         d.update({i:1})
# print(d)

# phonebook


# user={}

# 1.add contact {"name":"abc","phone":[12345,23456]}




# 04/07/2025


# set - mutable,unordered,elements- immutable, duplicates not allowed, indexing not possible

# set1=set()
# set2={10,"python",True,10,"python"}
# print(type(set2))
# print(type(set1))
# print(set2)

# list1=["python",10,"python",20,30,10]
# set1=set(list1)
# print(list(set1))

# set1={"python",10,"python",20,30,10(1,2,3)}
# print(set1)


#set methods

# add() - immutable arguments
# set1={10,20,30,40}
# set1.add("python")
# set1.add(100)

# set1.update(("a","b","c"))
# set1.update("django")
# print(set1)

# set1={10,20,30,40,"a"}
# # remove()
# set1.remove(10)
# # discard()
# set1.discard(20)
# print(set1)
# # pop()
# print(set1.pop())
# print(set1)


# set1={1,2,3,4}
# set2={3,4,5,6}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.difference(set1))
# print(set2.symmetric_difference(set1))



# tuple - immutable,iterable, indexing, alicing, duplicates,datatypes-any

# t1=(10,20,30,40)
# t2=10,20,30,40
# t3=()
# t4=tuple()
# t5=(10,)
# t6=10,

# print(type(t1))
# print(type(t2))
# print(type(t3))
# print(type(t4))
# print(type(t5))
# print(type(t6))

# print(t1.index(20))
# print(t1.count(10))

# packing and unpacking

# numbers=(10,20,30,40)
# first=numbers[0]
# for i in numbers:
#     print(i)
#     a=i

# numbers=(10,20,30,40,50)
# a,b,c,*d=numbers
# a,b,*c,d=numbers
# *a,b,c,d=numbers
# print(a)
# print(b)
# print(c)
# print(d)

# name="abc"
# age=23
# # print(f"my name is {name} and my age is {age}")
# print("My name is {} and my age is {}".format(name,age)) # default formatiing
# print("My name is {1} and my age is {0}".format(age,name)) #positional formatting
# print("My name is {y} and my age is {x}".format(x=age,y=name)) #keyword formatting


# path=r"C:\newpython\task1"
# print(path)
