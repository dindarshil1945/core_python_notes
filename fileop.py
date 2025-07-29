# python file operation

# open(),read(),write(),rename(),remove(),close()

# open(filepath,mode)
# mode - r - read
# w - write

# f=open(r"C:\Users\ASUS\Desktop\Luminar Notes.txt","r")
# # print(f.write("hw hwllo"))
# print(f.read())
# f.close()

# with open(r"C:\Users\ASUS\Desktop\Luminar Notes.txt","r") as f:
#     print(f.read())

# f=open("file1.txt","w")
# f.write("hello")
# f.close()

# EOF- \n 

# f=open("file1.txt","r")
# print(f.read(2))
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# f.close()


# f=open("file1.txt","w")
# f.writelines(["hello\n","hii\n","bye"])


# f=open("file1.txt","r")
# lines=f.readlines()
# # print(lines)
# print(len(lines))


# f=open("file1.txt","r")
# first_lines=f.readline()
# word_count=first_lines.split()
# print(len(word_count))



# f=open("file1.txt","r")
# print(len(f.readline().split()))



# f=open("file1.txt","r")
# content=f.read()
# words=content.split()
# print(len(words))
# # print(words)




# words that starts with i

# f=open("file1.txt","r")
# content=f.read()
# f.close()

# count=0
# words=content.lower().split()

# for i in words:
#     if i.startswith("i"):
#         count+=1

# print(count)



# lines that start with i

# f=open("file1.txt","r")
# line=f.readlines()
# count=0
# for i in line:
#     if i.startswith("I") or i.startswith("i"):
#         count+=1
# print(count)


# f=open("file1.txt","r+") #read/write
# print(f.read())
# f.write("hello")

# f=open("file1.txt","w+") #read/write
# # print(f.read())
# f.write("hello")
# print(f.read())

# try,except,finally,else

# n1=int(input("Enter num: "))
# n2=int(input("Enter num: "))

# try:
#     print(n1/n2)
# except:
#     print("error")
# print(n1*n2)


# n1=int(input("Enter num: "))
# n2=int(input("Enter num: "))

# try:
#     n1/n2
# except:
#     print("error")
# else:
#     print(n1/n2)
# finally:
#     print("final block")
# print(n1*n2)

# n1=int(input("Enter num: "))
# n2=int(input("Enter num: "))

# try:
#     print(n1/n2)
#     print(x)
#     print(n1.upper())
# except ZeroDivisionError:
#     print("Zero Division Error")
# except NameError:
#     print("Name error")
# except:
#     print("Somthing else")

import os
if os.path.exists("test1.txt"):
    os.remove("test1.txt")
else:
    print("no file")

# if os.path.exists("test.txt"):
#     os.rename("test.txt","test1.txt")