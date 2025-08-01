# num=int(input("enter a number: "))
# prime=True
# if num<=1:
#     prime=False
# else:
#     for i in range(2,num):
#         if num%i==0:
#             prime=False
#             break
# if prime:
#     print("prime")
# else:
#     print("not prime")

# n=int(input("Enter number: ")) #5

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if (i+j)%2==0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()



# n=int(input("Enter range: "))

# a=0
# b=1

# for i in range(n):
#     print(a)
#     temp=a
#     a=b
#     b=temp+a

# s = input()
# reversed_str = ""
# for i in s:
#     # print(i)
#     reversed_str = i + reversed_str  # prepend each char
# print(reversed_str)


# s=input("enter a string: ")
# vowels=0
# consonents=0
# for i in s:
#     if i in ["a","e","i","o","u"]:
#         vowels+=1
#     else:
#         consonents+=1
# print(f"Vowels: {vowels}")
# print(f"consonents: {consonents}")


# list1=[1,2,1,1,2,3,4,3,4]
# print(list(set(list1)))

# f=open("file.txt","r")
# content=f.read()
# words=content.split()
# print(len(words))

# try:
#     a = int(input("Enter numerator: "))
#     b = int(input("Enter denominator: "))
#     result = a / b
#     print("Result:", result)

# except ZeroDivisionError:
#     print("Error: Cannot divide by zero.")

# except ValueError:
#     print("Error: Please enter valid numbers.")
