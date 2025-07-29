# Question

# Write program to checka number is even or odd

# Code

# num=int(input("Enter a Number: "))
# if num%2==0:
#     print(f"{num} is an Even Number")
# else:
#     print(f"{num} is an Odd Number")


# Question

# Write a program to check whether given year is leap year or not

#code

# year=int(input("Enter Year: "))
# if (year%4==0 and (year%100!=0 or year%400==0)):
#     print(f"{year} is a Leap Year")
# else:
#     print(f"{year} is not a Leap Year")



# Question

# Write a program to find greatest number among three numbers

# code

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))

# if a>=b and a>=c:
#     print(f"{a} is largest")
# elif b>=a and b>=c:
#     print(f"{b} is largest")
# else:
#     print(f"{c} is largest")


# Question

# Accept the age, sex ('M', 'F'), number of days and display the wages accordingly


# code 

# age=int(input("Enter Age: "))
# gender=input("Enter Gender: ").upper()
# days=int(input("Enter Number of Days Worked: "))
# wage=0

# if age>=18 and age<30:
#     if gender=="M":
#         wage=700
#     elif gender=="F":
#         wage=750
#     else:
#         print("Invalid Gender")
# elif age>=30 and age<=40:
#     if gender=="M":
#         wage=800
#     elif gender=="F":
#         wage=850
#     else:
#         print("Invalid Gender")
# else:
#     print("Cannot Calculate")

# print(f"Daily wage: {wage}")

# if age>=18 and age<=40 and (gender=="M" or gender=="F"):
#     total_wage=days*wage
#     print(f"Total wage of {days} days: {total_wage}")


# age=int(input("Enter Age: "))
# sex=input("Enter Gender (M/F): ").upper().strip()
# days=int(input("Enter number of days worked: "))

# if (age>=18 and age<=40) and (sex=="M" or sex=="F") and (days>0):
#     if age>=18 and age<30:
#         if sex=="M":
#             wage=700
#             print(f"Total wage is ",wage*days)
#         else:
#             wage=750
#             print(f"Total wage is ",wage*days)
#     else:
#         if sex=="M":
#             wage=800
#             print(f"Total wage is ",wage*days)
#         else:
#             wage=850
#             print(f"Total wage is ",wage*days)
# else:
#     print("Cannot Calculate")


# Q5

# quantity=int(input("Enter quantity of purchased goods: "))
# unit_price=100
# total_amount=unit_price*quantity
# print(f"Total bill: {total_amount}")

# if total_amount>1000:
#     discount_amt=total_amount*0.10
#     amt_after_disc=total_amount-discount_amt
#     print(f"Discount: ₹{discount_amt}")
#     print(f"Total bill after discount: ₹{amt_after_disc}")

# Q6

# a=float(input("Enter first side: "))
# b=float(input("Enter second side: "))
# c=float(input("Enter third side: "))

# if a+b>c and b+c>a and a+c>b:
#     if a==b and b==c and c==a:
#         print("It is a Equilateral Triangle")
#     elif a==b or b==c or c==a:
#         print("It is a Isosceles Triangle ")
#     else:
#         print("It is a Scalene Triangle")
# else:
#     print("Cannot form a Triangle")

# Q7

# a=float(input("Enter first number: "))
# b=float(input("Enter second number: "))
# operator=input("Enter operator (+,-,*,/,%): ")
# result=0
# if operator=="+":
#     result=a+b
# elif operator=="-":
#     result=a-b
# elif operator=="*":
#     result=a*b
# elif operator=="/":
#     if b!=0:
#         result=a/b
#     else:
#         result="Error: Divison by zero"
# elif operator=="%":
#     if b!=0:
#         result=a%b
#     else:
#         result="Error: Modulo by zero"
# else:
#     result="Invalid Operator"
  
# print(result)


# Q8

# marks = float(input("Enter your marks: "))

# if marks < 0 or marks > 100:
#     print("Invalid marks! Please enter a value between 0 and 100.")
# elif marks < 25:
#     print("Your Grade is: F")
# elif marks < 45:
#     print("Your Grade is: E")
# elif marks < 50:
#     print("Your Grade is: D")
# elif marks < 60:
#     print("Your Grade is: C")
# elif marks < 80:
#     print("Your Grade is: B")
# else:
#     print("Your Grade is: A")

# Q9

# city = input("Enter city name (Delhi, Agra, Jaipur): ").strip().lower()

# if city == "delhi":
#     print("Monument: Red Fort")
# elif city == "agra":
#     print("Monument: Taj Mahal")
# elif city == "jaipur":
#     print("Monument: Jal Mahal")
# else:
#     print("information not available")

# Q10

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

if length == breadth:
    print("It is a Square.")
else:
    print("It is a Rectangle.")