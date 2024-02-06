#  a=input("Enter your name:")
#  print("My name is", a)

#  X=int(input("Enter your 1st number:"))
#  Y=int(input("Enter your 2nd number:"))
#  print(X+Y)
# print(X-Y)
# print(X*Y)
#  print(X/Y)

#  name = "Laly"
#  friend = "Pratham"
#  other_friend = "Nidhi"
#  apple = '''Hello everyone He said,
#  Hello My self Andry 
#  I want to eat apples'''

#  print("Hello " + name)
#  print(apple)
#  print(friend[4])
#  print(name[3])
#  print(other_friend[3])

#  for character in apple:
#   print(character)

# name ="andry,khushi,nikita,arya "
# print(len(name))
# print(name[0:-3])
# print(name[0:4])
# print(name[-6:-3])
# print(name[-20:-1])

# nm ="harry"
# print(nm[-4:-2])
# print(len(nm))




#day13
#Strings are immutable
# a = "!!Andry!!!!Andry"
# b = "Andry"
# print(len(a))
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!"))
# print(a.replace("Andry", "Pratham"))
# print(a.split("y"))
# blogHeading = "introduction to js"
# print(blogHeading.capitalize())

# str1 = "Welcome to Andry's blog"
# print(len(str1))
# print(len(str1.center(50)))
# print(a.count("Andry"))

# str1 = "Welcome to Andry's blog !!!"
# print(str1.endswith("!!!"))
# print(str1.startswith("!!!"))
# print(str1.endswith("to",4,10))

# str1="He's name is Dan. He is an honest man"
# print(str1.find("ishh"))

# str1 = "Welcome to Andry's blog"
# print(str1.isalnum())
# str1 = "Welcome"
# print(str1.isalpha())

# str1 = "hello world"
# print(str1.islower())
# str1 = "We wish you a Merry christmas\n"
# print(str1.isprintable())
# str1 = "     "
# #using spacebar
# print(str1.isspace())
# #using tab
# str2 =" "
# print(str2.isspace())
# # print(str2.title())


#day14
# a = int(input("Enter your age:"))
# print("Your age is:",a)
# if a>=18:
#   print("you can drive")
#   print("Yes")
# else:
#   print("You can not drive ")

# num = int(input("Enter the value of num:"))
# if(num<0):
#   print("Number is negative")
# elif (num == 0):
#   print("Number is zero")
# else:
#   print("Number is positive")

#Day15
 # a= int(input("Enter time"))
 # print("Time is:",a)
 # if( a>=4 and a<=12):
 #   print("Good Morning")
 # elif(a>=12 and a<=16):
 #   print("Good Afternoon")
 # elif(a>=16 and a<=18):
 #   print("Good Evening")
 # elif(a>=18 and a<=24):
 #   print("Good Night")
 # else:
 #   print("Are you single??")

# Day 16
# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%s')
# print(timestamp)


# #day16
# x = int(input("Enter the value of x:"))
# match x:
#   case 0:
#     print("x is Andry")
#   case 3:
#     print("case is 3")
#   case _ if x!=2:
#     print(x, "is not Nitya")
#   case _ if x!=4:
#     print(x, "is Lali")
#   case _:
#     print(x)


#day17
# name = "Arya," 
# for i in name:
#   print(i,)
#   if(i==","):
#     print("dii")
# name ="Niku,"
# for i in name:
#   print(i)
#   if(i==","):
#     print("dii")
# name= "Khushi,"
# for i in name:
#   print(i)
#   if(i==","):
#     print("papa ranjit")

# name= "vaibhav,"
# for i in name:
#   print(i)
#   if(i==","):
#     print("kutta")

# for num in range(10):
#   print(num)

# Day18
# i = int(input("Enter the number:"))
# while(i<=39):
#     i = int(input("Enter the number:"))
#     print(i)
# print("done")
# count = -5 
# while (count<0):
#   print(count)
#   count = count + 1
# else:
#   print("I am inside else")

# do while loop is not suppoerted in python

# do:
# print("do while loop")
# while(i>0):
#   print(i)
  
  
# Day19
# for i in range(12):
#   if(i==10):
#      print("chal nikal") 
#      continue
#   print("5 X",i,"=", 5* i)

# i = 0
# while True:
#   print(i)
#   i = i + 1
#   if(i*20 == 60):
#     break

#day20
# def calculateGmean(a,b):
#   mean = (a-b)/(a+b)
#   print(mean)
# a = 3
# b = 4
# gmean1 = (a-b)/(a+b)
# print(gmean1)
# c = 4
# d = 6
# gmean2 = (c-d)/(c+d)
# print(gmean2)


# def calculateGmean(a,b):
#   mean = (a*b)/(a+b)
#   print(mean)
# calculateGmean(3,4)

# def issmaller(a,b):
#   if a<b:
#     print("it is smaller")
#   else:
#     print("it is not smaller")
# issmaller(4,5)  

# def islarger(a,b):
#   if a>b:
#     print("it is larger")
#   else:
#     print("it is not larger")
# islarger(4,5)

# def table(a):
#   for i in range(10):
#     print("5 X",i+1,"=", 5* i+1)
#     i = i+1
# table(10)    

#day21
# def avr(a = 5, b =6):
#   print("The avr is",(a+b)/2)
# avr()  

# def name(fname, mname= "Lali" ,lname="Dubey" ):
#   print("Hey",fname,mname,lname)
  
# name("Andry")  


#day22
# l = [3,4,5,6,7,8,"Harry", "True"]
# print(l)
# print(type(l))
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[5])
# print(l[0])
# print(l[:])
# print(l[1:-1])
# print(l[-1:1])
# print(l[0:8:3])
# if "Harry" in l:
#   print("yes")
# else:
#   print("no")
# if "arry" in "Harry":
#   print("yes")
# else:
#   print("no")
# if "i" in "Harry":
#   print("yes")
# else:
#   print("no")


# program to display prime number till N

# def is_prime(num):
#   if num<2:
#     return False
#   for i in range(2,int(num**0.5)+1):
#     if num%i==0:
#       return False
#     return True
#   N = 10 
#   print(f"Prime number till{N}:")
#   for i in range(2,N+1):
#     if is_prime(i):
#       print(i)

#day 23
# l =[11,45,1,2,4,6,1,1]
# print(l)
# l.append(5)
# print(l)
# l.sort(reverse =True)
# print(l)
# l.reverse()
# print(l.index(2))
# print(l.count(4))
# m= l.copy()
# print(l)
# m[0]=0
# print(l)
# l.insert(1,899)
# print(l)
# m=[900,1000,1100]
# l.extend(m)
# print(l)

# day 24
# tup =(1,2,3,4,5,6,7,8,9,10)
#tup[0]=2
# print(type(tup),tup)
# print(len(tup))
# print(tup[0])
# print(tup[-1])
# print(tup[2])
# print(tup[11])

# if 2345 in tup:
#   print("Yes 234 is present in this tuple")
#   tup2 = tup[1:4]
#   print(tup2)

# day25
tuple1 = (0,1,2,3,4,5,6,1,2,3)
tuple1.count(3)
tuple1.index(3)
tuple1.index(3,2)
