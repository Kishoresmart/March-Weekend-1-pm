#task1
#Get one string from user
name = input("Please enter the name: ")#kishore
count = len(name)
#identify the middle character of the string
middle = count//2
print(name[middle])#h

#Task2:
string1="***python***"
string2= "**python********"
string3= "********java*******"

print(string1.strip("*"))#python
print(string2.lstrip("*"))#python********
print(string3.rstrip("*"))#********java

#Task3:
#(name<space>float)
#collect three strings from user  name<space>float

a=input("Enter the subject and marks:")#telugu 93.5
b=input("Enter the subject and marks:")#english 94.5
c=input("Enter the subject and marks:")#hindi 93.2

a=a.split()
b=b.split()
c=c.split()
print(float(a[1])+float(b[1])+float(c[1]))#281.2

#Task4:
#collect two strings from user
#string1: python
#String2: java
#output ===> jythonpava64hv"

string1=input("enter the name:")
string2=input("enter the name:")
a=len(string1)
b=a//2
d=len(string2)
f=d//2
print(string2[0]+string1[1:]+string1[0]+string2[1:]+str(a)+str(d)+string1[b]+string2[f])

#Task5:
#collect two strings from user
#string1: maths
#String2: science
#output ===> sathsmcience57te

string1=input("enter the name:")
string2=input("enter the name:")
a=len(string1)
b=a//2
d=len(string2)
f=d//2
print(string2[0]+string1[1:]+string1[0]+string2[1:]+str(a)+str(d)+string1[b]+string2[f])

#Task6:
#Collect two strings from user
#string1: wikipedia
#string2: typescript
#output: p  +  c   ===> ascii value of p + ascii value of c  ====>  198
#(ord , chr)


string1 = input("enter the 1st word: ")#python
string2 = input("enter the 2nd word: ")#class

c1 = len(string1)
c2 = len(string2)
mid1 = c1//2
mid2 = c2//2
a = string1[mid1]
b = string2[mid2]

#Task7:
#collect one string from user:
#string: computer
#output: c6r	

a = input("Enter the one word: ")#python
b = len(a)
string1 = a[0]
string2 = a[b-1]
print(string1+str(b)+string2)#p6n

#Task8
Say hello world with python

print("Hello, World!")#Hello,world

#Task 9
#swapcase

name = "Python, Class "
swapping= name.swapcase()
print(swapping)#pYTHON, cLASS

#Task10:
#Mutation

string = input("Enter the string:")#phyton
string1  = list(string)
string1[4]='k'
string=''.join(string1)
print(string)#pythkn

#Task11:
#Arithmetic operator

a = int(input("enter one a value:")) #3
b = int(input("enter one b value:")) #2

print(a+b)#5
print(a-b)#1
print(a*b)#6

#Task12:
#python divison

a=int(input("enter one a value:"))#3
b=int(input("enter one a value:"))#5
c= a//b
d=a/b
print(c,d)#0,0.6