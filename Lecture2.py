#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:48:18 2022

@author: umamazillur
"""

#### fix the following errors!

#1
x = 10
y = 20
z= x+y
print(z)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list_len)

#3
my_string = 'hello world'
big_string = my_string.upper()
print(big_string)

#4
z = ['a', 'b', 'c']
z += 'd'
#z.append('d')

#5 why does the x not display 10, followed by the 200?  Fix it so it does.
x = 10
print(x)
y = 20
print(x * y)

#6
color = 'My favorite color is {}, what is yours?' % blue
print(color)

#### answer the following questions without changing the code given

#7 make the entries in this list unique
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
set(schools)
#not ordered 

#8 change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish'])
list(animals)


#9 make this string take a name based on a variable (you can modify the code on this one)
name = 'Sarah'
welcome = f'Hello {name}, and welcome to Data and Programming!'
print(welcome)

#10 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'I LOVE how spring is super late this year and there are no flowers and it is cold and rainy.'
lower_sent = my_sent.lower()
my_sent_list = [lower_sent]
print(my_sent_list)

my_sent.lower().split()


