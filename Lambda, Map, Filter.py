# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:06:13 2019

@author: Yeisson Alirio
"""
#Lambda - Basic Syntax
#lambda arguments : expression

EU_Dol = lambda x, y : x * y
#Taza de cambio Euro a Dolar 2.10.2019
rate=1.09
EU=input('Amount of EU to convert into USD: ')
#Convert input into a float_number
EU=float(EU)
EU_Dol(EU,rate)
result=str(EU_Dol(EU,rate))
print(result+' USD')


#Map -Basic Syntax
#map(function_object, iterable1, iterable2,...)

# using just one iterable
a=map(lambda x: x*rate, [1,2,3,4])
#map fnction returns an iterator - it can't be seen
#but can be transform into a list
list_a=list(a)
print (list_a)

#using 2 or more iterable
b=map(lambda x,y: x+y, [1,2,3,4], [3,2,1])
list_b=list(b)
#notice that operate i_x with i_y,
#in case of different length omite missin values
print (list_b)


#Filter - Basic Syntax
#filter(function_object, iterable)

a = [1, 2, 3, 4, 5, 6]
filter_c=filter(lambda x : x % 2 == 0, a) # Output: [2, 4, 6]
#filter fnction returns an iterator - it can't be seen, indexed of use len()
#but can be transform into a list
c=list(filter_c)
print(c)


#Filter lists of dicctionaries
dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]
filter(lambda x : x['name'] == 'python', dict_a) # Output: [{'name': 'python', 'points': 10}]


