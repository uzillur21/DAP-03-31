#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 15:04:57 2022

@author: umamazillur
"""

# PPHA 30535
# Spring 2021
# Homework 1

# UMAMA ZILLUR
# UZILLUR21

# Due date: Sunday April 10th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.

#create a list variable 
letters = ['a', 'b', 'c', 'd', 'e']

#a for loop thatobject and prints both these values
index = 0
for l in letters :
    print("The value at position {} is {}".format(index, l))
    index += 1    
#https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops

# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results of these
# four tests.

#a function that takes any string or list of strings and when applicable 
#removes special characters and spaces and capitalization
#if the string is a palindrome it returns true or else it returns false
def isPalindrome(str):
    #make all strings lowercase
    str = str.lower()
    #remove comma
    str = str.replace(',', '') 
    #remove exclamation point
    str = str.replace('!', '')
    #remove space
    str = str.replace(' ', '')
    #check if string is equal to the reversed order of the string (palindrome)
    if str == str[::-1]:
        return True
    return False  

isPalindrome('A man, a plan, a canal, Panama!')
isPalindrome('radar')
isPalindrome('Apple')
isPalindrome ('This isnt a palindrome')


#https://www.geeksforgeeks.org/check-linked-list-strings-form-palindrome/
#https://stackoverflow.com/questions/70829765/how-to-check-for-palindrome-ignoring-special-characters-and-case

# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.

#a list of strings which will be our available vegetable choices
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
#a new empty variable that is a placeholder for user vegetable choice
choice = ''
#a while loop which checks if user input is part of our list of vegetables and 
#only ends when user input is part of our list. 
while choice not in available_vegetables:
    #user input of vegetable choice 
   choice = input('Your choice is invalid. Please pick another choice')
#loop ends when available vegetable is chosen 
print('You can have the vegetable %s '%choice)

    
# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".

#create a list of strings
list_string = ['apple', 'banana', 'kristen', 'angel', 'bunny', 'ALTA']

#list comprehension that returns a new list with strings starting with the letters
# a or b and only if the string contains all lowercase letters
mapped = [i.startswith('a',0) or i.startswith('b',0) for i in list_string if i.islower()==True]
print(mapped)

#https://www.programiz.com/python-programming/methods/string/islower#:~:text=The%20islower()%20method%20returns,uppercase%20alphabet%2C%20it%20returns%20False.
#https://www.programiz.com/python-programming/methods/string/startswith

# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]

#create a list of integers
start_list = [3, 5, 7, 9, 11, 13]

#list comprehension that multiplies each object by 2 and rearrages objects in 
#descending order
new_list= [i*2 for i in start_list.reverse()]
print(new_list)


# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}

short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']

#dictionary comprehension that joins the two lists above and uses short_names 
#as key and long_names as value
my_dict = {short_names[i]:long_names[i] for i in range(len(short_names))}
print(my_dict)
#https://pythonguides.com/python-creates-a-dictionary-from-two-lists/




