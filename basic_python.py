# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:40:33 2024

@author: Sai
"""
################################### 1st lec #############################
##print() function
print("Hello world")
print("Hello my name is Anushka.", "My age is 20")
print(23)
print(23+2)
##variable
name = "Anushka"      #string
age = 20              #integer
price = 25.99         #float
print("My name is: ",name)
print(age)
print(price)
print(price,age)
age2 = age
age2
##type()
print(type(name))
print(type(age))
print(type(price))
name1='Anu'
name2="Anu"
name3='''Anu'''
print(name1,name2,name3)
###boolean and none data type
old=False
a=None
print(type(old)) 
print(type(a))  
##########sum code
a=2000
b=5000
sum=a+b
print(sum)      
###operators
##arithmetic op
    a=10
    b=2
    print(a+b)
    print(a-b)
    print(a/b)
    print(a%b)
    print(a ** b)
#####relational\comparision op
      a=10
      b=20
      print(a==b)
      print(a!=b)
      print(a<b)
      print(a>b)
      print(a<=b)
      print(a>=b)
##### assignment op
    num=10
    print(num)
    num+=10         #num=num+20
    print(num)     
    num-=5
    print(num)
    num/=5
    print(num)
    num**=2
    print(num)
    num%=5
    print(num)
####logical op
    print(not False)
    print(not True)
    val1=True
    val2=True
    print("Ans operator ",val1 and val2)    ##if both values are true 
    print("ans operator ",val1 or val2)     ##if any one value is true
####type conversion
#1.type conversion    
    a=10
    b=12.3
    sum=a+b
    sum
#2.type casting
    a=10
    b="20"
    c=int(b)
    sum=a+c
    print(sum)      
##input()---Accept input from user
name=input("Enter ypur name: ")      
print("welcome ,",name)
print(type(name),name)
input("Enter ur age: ")
#####################practice que#######################
#program to input 2 no. and print their sum
a=int(input("Enter 1st no. : "))
b=int(input("Enter 2nd no.: "))
c=a+b
print("Sum= ",c)
#to i/p side of square & print its area
a=int(input("Enter side: "))
area=a*a
print("Area= ",area)
#to i/p 2 float point no. and print their avg
a=float(input("Enter 1st no.: "))
b=float(input("Enter 2nd no.: "))
avg=(a+b)/2
print("Average= ", avg)


'''to i/p 2 int no. a,b print true if a is greater or equal to b,
 if not print false '''
 a=int(input("Enter 1st no. :" ))
 b=int(input("Enter 2nd no. : "))
 print(a>=b)

################################# 2nd Lec ##################################### 
str1="This is a string"
str2='This is a string'
str3='''This is a string'''
print(str1,"\t",str2,"\n",str3)
####string operation####]
#concatination
str1="This is"
str2="String"
final_str=str1+" "+str2
print(final_str)
#lenght len()
lenght1=len(str1)
print("Length= ",lenght1)
####Indexing
Str1="This is my first index"
str1[2]      #o/p is 'i'           
#####slicing
str1="data science for python"
print(str1[0:3])
print(str1[0:4])
print(str1[5:len(str1)])
print(str1[5:])
print(str1[:5])
######negative indexing
str1="This is my string"
str1[-5:-1]
######string function
str1="i am a coder"
#endswith()
str1.endswith("er")         #true
str1.endswith("am")         #false
#capitalize()
str1.capitalize()           #'I am a coder'
#replace()
str1.replace('a','A')
str1.replace('coder', 'learner')
#find()
str1.find('am')
str1.find('m')
str1.find('q')
#count()
str1.count('am')
str1.count('a')
str1.count('q')         #it is not exist then return 0
##########################practice que on strings#####################
#to i/p user 1st name and print its length
name=input("Enter your 1st name: ")
print("Length of name: ",len(name))
#to find no. of occuerences of 's' in astring
str1="Hii I am the $19$80"
print("No. of occerences: ",str1.count('$'))
##########conditional statements
age=int(input("Enter age: "))
if age>18:
    print("\nEligible for voting")
else:
    print("Not eligible for voting")
#############
light="green"
if light == 'red' :
        print("stop")
elif light == 'green' :
        print("go")
elif light == 'yellow' :
        print("wait")
else :
        print("other")
print("End of code")
##############
marks=int(input("Enter marks of stud: "))
if marks>=90:
    print("Grade A")
elif marks<90 and marks>=80 :
    print("Grade B")
elif marks<80 and marks>=70:
    print("Grade C")
elif marks<70 and marks>=60:
    print("Grade D")
else:
    print("marks is less than 60")
##########nesting if statement####
age = 12
if age>=18:
    if age>=80:
        print("can not drive")
    else:
        print("can drive")
else:
    print("cannot drive")
#####################################lec 3#####################################
########List
marks=[12.2,13.3,33.4]
marks
print(type(marks))
print(marks[0], " and " ,marks[2])
stud=['Anu',89,'Sam',88]
stud
stud[0]='Anushka'
stud
m=[1,2,3,4,5,6]
print(m[1:4])
print(m[1:])
print(m[:3])
print(m[-3:-1])     #negative slicing
########list methods
list=[2,1,4,3,1]
list
list.append(5)
list
print(list.sort())          #ascending order sorting
list
list.sort(reverse=True)     #descending order sorting
list
l1=['apple','mango','banana']
l1.sort()
l1
list.reverse()
list
l1.reverse()
l1
list.insert(1,11)
list
list.remove(1)
list
list.pop(0)
list
######################Tuple
tuple=(1,4,3,2,5)
print(tuple)
print(type(tuple))
######tuple slicing
print(tuple[1:3])
print(tuple[-3:-1])
########tuple methods 
tup=(1,5,3,4,1)
tup.index(1)
tup.count(1)
tup.count(3)

######################################## lec 04 ################################
#########dictionary
dict={"name":"Anushka","CGPA":8.9,"subjext":['java','cpp','c'],"topics":('dict','set')}
dict
print(type(dict))
###accessing values
print(dict["name"])
dict["name"]="Anu"
dict
dict[1]='a'
dict
null_dict={}            #NUll dictionary
null_dict
##nested dictonary
stud={"name":"Anushka","score":{"math":88,"SEN":90,"STE":99}}
print("Nested dict: ",stud)
print(stud["score"]["SEN"])
####dictionary methods
d={1:'a',3:'e',2:'d',4:'b'}
d
d.keys()
stud.keys()
print(list(stud.keys()))        ###dict to list using keys()
len(d)          ##lenght of dict

d.values()
stud.values()
print(list(stud.values()))    ##dict to list using values()

d.items()
stud.items()
print(list(stud.items()))       ##dict to list using items()

##returning values using keys
d.get(1)        #In this method if key is not exist then it just print 'none'
d[1]            #here if key is not present then it gives an error

d.update({'city':'Pune'})
print (d)

################# Set in python
s={1,2,1,"Hello",45.5}
print(s)        #repeated values stored only once
print(len(s))
print(type(s))
s1=set()
print(type(s1))
####set methods
s1={1,8,3,6,72,6,9}
s1
s1.add(101)
s1
s1.remove(1)
s1
s1.add(("hello","wel-come"))
s1
s1.pop()
s1
s1.clear()
s1

set1={11,34,22,55}
set2={55,34,77,88}
set1.union(set2)
set1.intersection(set2)
################################ lec 05 #######################################
##loops in python 
#1) while loop
#2) for loop
count = 1
while count<=5:
    print("Hello")
    count+=1
##print no. 1 to 5
i = 1
while i<=5:
    print("Number = ",i)
    i+=1
##print no. reverse 5 to 1
i = 5
while i>=1:
    print("Number = ",i)
    i-=1
print("loop end")
###break keyword
i = 1
while i<=5:
    print("Number = ",i)
    if(i==3) :
        break
    i+=1
print("end of loop")

nums=[11,22,33,44,5,51]
x=44
i=0
while i<len(nums):
    if(nums[i]==x):
        print("number found at index: ",i)
        break
    else : 
        print("finding")
    i+=1
##continue keyword
i = 1
while i<=5:
    if(i==3):
        i+=1
        continue
    print("Number = ",i)
    i+=1
#odd no. and skip even no.
i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue     #skip
    print("Odd numbers: ",i)
    i+=1
##for loop
no=[1,2,3,4]
for val in no:
    print(val)
    
tup=('a','b','c','d')
for i in tup:
    print(i)

str="This is str"
for i in str:
    print("String char(it also print white spaces): ",i)

str="This is str"
for i in str:
    if(i=='i'):
        print("char: i found")
        break
    print("String char(it also print white spaces): ",i)
else:
    print("end")

##range() function
print(range(5))

seq=range(5)
for i in seq:
    print(i)

for i in range(1,10,2):    #start=1, stop=10, step=2
    print(i)
    
##pass statement
for i in range(10):
    pass
    if i<5:
        pass
print("some useful work")
##################################### lec-06 ##################################
##function
def sum(a,b):       #function defination
    sum=a+b
    return sum
sum(10,1)           #function call
sum(23,4)   

def cal_sum(x,y):
    return x+y
cal_sum(90,0)     
    
def print_hello():
    print("HELLO")
print_hello()

#average of 3 numbers
def average(a,b,c):
    return(a+b+c)/3
average(90,89,99)

#default parameter
def cal_mul(a=7,b=7):
       print(a*b)
       return a*b
cal_mul()
cal_mul(12,12)
    
##Recursion function 
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5) #5,    4=n-1,  3=n-2,  2=n-3, 1  ##It calls the recursion function repetativly

##factorial code in recursion
def fact(n):
    if (n==0 or n==1):
        return 1
    return fact(n-1)*n
fact(5)
################################## lec-07 #####################################
##file input/output in python
f=open("F:\pra.txt","r")
data=f.read()           #read file contents
print(data)
print(type(data))
data=f.read(2)
print(data)
line1=f.readline()
line2=f.readline()
print(line1)
print(line2)
f.close()

f=open("F:\pra.txt","w")
f.write("This is the WRITE mode.\nFile open in write mode.")
f.close()

f=open("F:\pra.txt","a")
f.write("\nThis is the APPEND mode.")
f.close()
## with syntax
with open("F:\pra.txt","r") as f:
    data=f.read()
    print(data)

with open("F:\pra.txt","w") as f:
    f.write("This file is open by using with syntax.")
    print(data)

#deleting file
import os
os.remove("F:\del.txt")

###################################### lec-08 #################################
#OOP concepts --- classes, objects, constructor, static method
class stud:
    name="Anushka"
s1=stud()
print(s1.name)

class car:
    color="blue"
    model="new"
    brand="BMW"
c1=car()
print(c1.color)
print(c1.brand)
print(c1.model)

##__init__ function
class stud:
    name="Anushka"
    def __init__(self):
        print(self)
        print("Adding new stud in database: ")
s1=stud()
print(s1.name)
print(stud.name)

class student:
    def __init__(self,fullname):
        print("Adding new stud in DB: ")
        self.name=fullname
s=student("Anushka")
print(s.name)

##method
class stud:
    def __init__(self,name):
        self.name=name
    def hello(self):
        print("say hello to: ",self.name)
s1=stud("karan")
s1.hello()

##static method
class stud:
    @staticmethod
    def hello():
        print("Say hello")
s1=stud()
s1.hello()

##4 pilors in OOP: Abstraction, Encapsulation, Inheritance, Polymorphism
##Abstraction
class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True      #This details are hide 
        self.acc=True         #--------""----------
        print("car started...")    #only this sentence is print
c1=car()
c1.start()

##Encapsulation





## del keyword
class stud:
    def __init__(self,name):
        self.name=name
s1=stud("Anushka")
del s1
print(s1)     #it gives error bez s1 obj is deleted (NameError: name 's1' is not defined)
        
##private attribute and methods
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass  #the meaning of __(double underscore) is private variable for this class 
    def reset_pass(self):
        print(self.__acc_pass)#this variable does not access outside class it access using this method bez this method present inside class
acc1=account("1234","abcd")
print(acc1.acc_no)                                     
print(acc1.reset_pass())

class person:
    __name="anonymous"
    def __hello(self):
        print("Say hello")
    def welcome(self):
        self.__hello()
p1=person()
print(p1.welcome())

##Inheritance & super method
class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
             
    @staticmethod
    def stop():
        print("car stopped")
class Toyotacar(car):
    def __init__(self,name,type):
        super().__init__(type)
        super().start()
        self.name=name
car1=Toyotacar("Fortuner","new")
car1.stop()
car1.start()
print(car1.name)
print(car1.type)
print(car1.name)


#multi-level inheritance
class A:
    var1="Welcome to class A"
class B:
    var2="Welcome to class B"
class C(A,B):
    var3="Welcome to class C"
c1=C()
print(c1.var1)
print(c1.var2)
print(c1.var3)

#class method
class person:
    name="sai"
    @classmethod
    def changeName(cls,name):
        cls.name=name
p1=person()
p1.changeName("Om")
print(person.name)

# @property decorator
class stud:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
        #self.per=str((self.phy+self.chem+self.math)/3)+" %"
    #def cal_per(self):
        #self.per=str((self.phy+self.chem+self.math)/3)+" %"
#this code is replace by @property decorator
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+" %"
s1=stud(90,89,96)
#print(s1.per)
s1.phy=99
print(s1.percentage)
#print(s1.cal_per())
#print(s1.per)

#Polymorphism
##operator overloading
print(1+2)#3
print("Anu"+" Cholke")      #concatenation
print([1,2,3]+[4,5,6])#merge

#complex number addition
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNum(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self,num2):          #__add__()---->It is the dunder function
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return complex(newReal, newImg)
num1=complex(1,3)
num1.showNum()

num2=complex(4, 6)
num2.showNum()

num3=num1.add(num2)
num3.showNum()

num3=num1+num2    #this is using dunder function
num3.showNum()

################################# PRACTICE QUESTIONS ##########################
#1. write a program to input 2 no. and print their sum
a=int(input("Enter 1st num :"))
b=int(input("Enter 2nd num: "))
sum=a+b
print("Sum= ",sum)

#2. WAP to i/p side of a square & print its area
side=int(input("Enter side of square: "))
area=side*side
print("Area of square is: ",area)

#3. WAP to i/p 2 floating point no. and print their average
a=float(input("Enter 1st num: "))
b=float(input("Enter 2nd num: "))
avg=(a+b)/2
print("Average is: ",avg)

#4.WAP to i/p 2 int num a & b. Print True if a is greater or equal to b. If not then print False
a=int(input("Enter 1st num: "))
b=int(input("Enter 2nd num: "))
print(a>=b)
                                ## OR ##
if a>=b:
    print("True")
else: 
    print("False")

#5. WAP to check num entered by user is odd or even
a=int(input("Enter number to check if it is even or odd: "))
if(a%2==0):
    print("Entered number is even.")
else:
    print("Entered number is odd.")

#6. WAP to find greatest of 3 numbers entered by the user
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
if (a>b) and (a>c):
    print("A is greater")
elif (b>a) and (b>c):
    print("B is greater")
elif (c>a) and  (c>b):
    print("C is greater")
else:
    print("All A, B and C are equal")

#7. To check if number is a multiply of 7 or not
a=16
if a % 7 == 0:
    print("Number is multiply by 7")
else:
    print("Number is not multipy by 7")
    
#8. WAP to ask user to enter names of their 3 favorite movies and store them in a list
mov1=input("Enter 1st favorite movie name: ")
mov2=input("Enter 2nd favorite movie name: ")
mov3=input("Enter 3rd favorite movie name: ")
list1=[mov1,mov2,mov3]
print(list1)
print(type(list1))    

#9. WRA to check if a list contains a palindrome of elements.(Hint:use copy() method)
list1=[1,2,3]
copy_list=list1.copy()
copy_list.reverse()
if (copy_list==list1):
    print("List is palindrome")
else:
    print("List is not a palindrome")
    
#10. WAP to count the number of student with the "A" grade in the foll. tuple 
#    ["C","D","A","A","B","B","A"]
tup=('C','D','A','A','B','B','A')
print("The number of student with grade is: ",tup.count('A'))

#11. Store the above values in a list & sort them from "A" to "D"
list1=['C','D','A','A','B','B','A']
list1.sort()
print("Sorted list is: ",list1)    

#12. store the foll. word meanings in python dictionary:
    #table:"A piece of furniture","list of fact & figures"
    #cat:"a samll animal"
dict1={'cat':'a small animal','table':['A piece of furniture','list of fact & figures']}
print(dict1)

#13.You are given a list of subjects for stud. Assume one classroom is required for 1 sub.
#How many classroom are nested by all stud.
   #"python","java","c++","javascript"
   #"java","python","c++","c"
set1={"python","java","c++","javascript","java","python","c++","c"}
print("Number of classroom required is: ",len(set1))

#14.WAP to enter marks of 3 sub from user & store them in a dictionary. 
#Start with an empty dictionary & add one by one. Use subject as key & marks as value. 
marks={}
chem=int(input("Enter mark of chem sub: "))
marks.update({'chem':chem})
phy=int(input("Enter marks of phy sub: "))
marks.update({'phy':phy})
math=int(input("Enter marks of math sub: "))
marks.update({'math':math})
print(marks)

#15. Figure out a way to store 9 & 9.0 as seprate values in the set.
#(you can help of built-in data types)
values={9,"9.0"}
print(values)
            # OR #
values={("float",9.0),("int",9)}
values

#16. print the no. from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1

#17. print no. from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1

#18. print the multiplication table of a number n
n=3
i=1
while i<=10:
    print(n*i)
    i+=1

#19. print the element of foll. list using a loop:[1,4,9,16,25,36,49,64,81,100]
list=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx < len(list):
    print(list[idx])
    idx+=1

#20.Search for a number x in this tuple using loop:(1,4,9,16,25,36,49,64,81,100)
tup=(1,4,9,16,25,36,49,64,81,100)
i=0
x=36
while i < len(tup):
    if tup[i]==x:
        print("found at index ",i)
    i+=1

#21. print the ele of foll. list using a loop:[1,4,9,16,25,36,49,64,81,100]
list=[1,4,9,16,25,36,49,64,81,100]
for i in list:
    print(i)
    
#22. search for a no. x in this tuple using loop: [1,4,9,16,25,36,49,64,81,100]
tup=(1,4,9,16,25,36,49,64,81,100)
x=25
idx=0
for i in tup:
    if i==x:
        print("Number is found at index ",idx)
    idx+=1
        
#23.print numbers from 1 to 100
i=1
for i in range(1,101):
    print(i)

#24.print number from 100 to 1
for i in range (100,0,-1):
    print(i)
    
#25.print the multiplication table of the num n
n=int(input("Enter num to print multiplication table: "))
for i in range(1,11):
    print(n*i)
    
#26.WAP to find sum of first n numbers.(Using while loop)
n=int(input("Enter value of n: "))
i=1
sum=0
while i <= n:
    sum += i
    i += 1
print(sum)
    
#27.WAP to find factorial of first n numbers (using for loop)
n=int(input("Enter the value of n: "))
fact=1
for i in range(1,n+1):
    fact *= i
print("Factorial = ",fact)

#28.write a function to print the length of list (list is the paramenter)
list=['A','B','C','D','E','F']
def print_len(list):
    print(len(list))
print_len(list)

#29.WAF to print ele of a list in a single line.(list is the paramenter)
list=['A','B','C','D','E','F']
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(list)

#30.WAF to find the factorial of n.(n is the parameter)
n=5
def factorial(n):
    fact=1
    for i in range (1,n+1):
        fact *= i
    print("factorial: ",fact)
factorial(5)

#31. WAF to convert USD(american doller) to INR(indian rupee)  1 doller = 83 rupee
def converter(USD):
    INR=USD*83
    print(USD,"USD =",INR ,"INR")
converter(2)

#32. Write a recursive function to calculate sum of first n natural number
def sum(n):
    if n==0 :
        return 0
    return sum(n-1)+n
cal_sum=sum(10)
print(cal_sum)

#33.write a recursive fun to print all ele in a list (hint:use list & index as paramenter)
def print_ele(list,idx=0):
    if idx==len(list):
        return 
    print(list[idx])
    print_ele(list,idx+1)
l=['A','B','C','D','E','F']
print_ele(l)

#34. Create a new file "practice.txt" using python. Add foll data in it:
'''Hi everyone 
   we are learning file I/O
   using Java.
   I like programming in Java.'''
with open("practice.txt","w") as f:
    f.write("Hi everyone")    
    f.write("\nwe are learning file I/O")
    f.write("\nusing Java")
    f.write("\nI like programming in Java.")

#35.WAF that replace all occurrences of 'java' with 'python' in above file
with open("practice.txt","r") as f:
    data=f.read()
    new_data=data.replace("Java", "Python")
    print(new_data)
#now overrite file with new_data
with open("practice.txt","w") as f:
    f.write(new_data)
    
#36.search if the word "learning" is exist in the file or not
with open("practice.txt","r") as f:
    data=f.read()
    if data.find("learning") != -1:
        print("found")
    else:
        print("not found")
    
#37.WAF to find which line of file does the word "learning" occur first. Print -1 of word not found.
def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if (word in data):
                print(line_no)
            line_no+=1
    return -1
check_for_line()
    
#38.From a file containing no. seprated by comma,print the count of even no.
count=0
with open ("practice.txt","w")as f:
    f.write("1,2,76,84,90,101")    
with open ("practice.txt","r")as f:
    data=f.read()
    nums=data.split(",")
    for val in nums:
        if (int(val)%2==0):
            count+=1
print(count)

#39.create a stud class that take name & marks of 3 subjects as argument in constructor.
#Then create a method to print avg
class stud:
    def __init__(self,name,chem,phy,math):
        self.name=name
        self.chem=chem
        self.phy=phy
        self.math=math
    def average(self):
        sum=self.chem+self.phy+self.math
        print("Average= ",sum/3)
s1=stud("Anushka",99,90,98)
print(s1.name)
s1.average()

#40.create account class with 2 attribute-balance & account no. Create method for debit,credit & printing the balance
class account:
    def __init__(self,bal,acc_no):
        self.bal=bal
        self.acc_no=acc_no
    def debit(self,amt):
        self.bal-=amt
        print("Rs. ",amt," was debited")
    def credit(self,amt):
        self.bal+=amt
        print("Rs. ",amt," was credited")
    def get_bal(self):
        print("Total balance is: ",self.bal)
a1=account(200000,"AR1234")
a1.debit(1000)
a1.credit(9000)
a1.get_bal()
        
#41.Define a class circle to create circle with radius r using the constructor. 
#Define an Area()method of class which calculate area of circle.
#Define a Perimeter() method of class which allows you to calculate perimeter of circle
class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        print("Area of circle is: ",3.14*self.r*self.r)
    def perimeter(self):
        print("Perimeter of circle: ",2*3.14*self.r)
c1=circle(12)
c1.area()
c1.perimeter()
        
#42.Define a employee class with attribute role,department,sal.This class alse having showDetail(method)
#create an engineer class that inherits properties from employee & has additional attributes:name & age
class employee:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal
    def showDetail(self):
        print("Role: ",self.role)
        print("Department: ",self.dept)
        print("Salary: ",self.sal)
class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","Computer",50000)
eng1=engineer("Anushka", 20)
eng1.showDetail()       

#43.Create a class order which store item & its price. Use Dunder function __gt__() to convey that:
#order1>order2 if price of order1>price of order2
class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,odr2):
        return self.price > odr2.price
odr1=order("chips",15)
odr2=order("Tea",20)
print(odr1>odr2)