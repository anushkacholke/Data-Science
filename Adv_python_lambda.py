# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:12:58 2024

@author: Sai
"""

sum=lambda a,b:a+b
print(sum(10,8))

(lambda x,y : x*y)(5,7)

add=lambda x,y=9,z=1 : x+y+z
print(add(2))

higher_ord_fun = lambda x , fun : x + fun(x)
higher_ord_fun (20, lambda x : x*x )

(lambda x : x%2 and 'odd' or 'even') (21) 

sub_string=lambda string:string in "Welcome to python function"
print(sub_string('python'))

#filter()
num=[12,30,60,2,14,17,90,80]
greater=list(filter(lambda num:num>30,num))
print(greater)

less_than=list(filter(lambda num:num<30,num))
print(less_than)

divide=list(filter(lambda x:(x%4==0),num))
print(divide)


#map()
double_the_num=list(map(lambda x:x*2,num))
print(double_the_num)

n=[2,3,4]
list_of_cube=list(map(lambda x:pow(x,3),n))
print(list_of_cube)


##reduce function
from functools import reduce
list1=[2,5,7,8]
sum=reduce((lambda x,y : x+y),list1)
print(sum)

#quadratic function
def quadratic(a,b,c):
    return lambda x : a*x**2 + b*x + c
f=quadratic(2, 3, 5)
f(0)         # 0 is the value of x

















