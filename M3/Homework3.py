#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:29:17 2021
Homework# Python
@author: dmitrymikhaylov
UVA ID: agp7dp
"""

#Q1: Dictionary basics: (2 pts)
 
# Create a dictionary of 10 key-value pairs. Choose a domain that interests you.
rgb_colors_dict = { "Black":(0,0,0),
 	"White":(255,255,255),
 	"Red":(255,0,0),
    "Lime":(0,255,0),
 	"Blue":(0,0,255),
 	"Yellow":(255,255,0),
 	"Cyan/Aqua":(0,255,255),
 	"Magenta/Fuchsia":(255,0,255),
 	"Silver":(192,192,192),
 	"Gray":(128,128,128)    
    }

#Demonstrate retrieving at least three different values. Display each of the results.
fav_colors = ["Black", "White", "Red"]
for color in fav_colors:
    print("My fav color "+color+" has the following RGB code: "+str(rgb_colors_dict.get(color)))




#Q2: Getting user input: (2 pts)

# Ask user for his or her name and two numbers (separately).
user_name = input("Please provide your name and 2 numbers. Name first: ")
numbers = input("Now, please provide the 2 numbers: ").split()
user_num1, user_num2 =  int(numbers[0]), int(numbers[1])

# Multiply the two numbers. Display the result as a floating-point number (not an integer).
result = float(user_num1 * user_num2)

# Display an output like the following: Hi, <NAME>! Multiplying <NUM1> and <NUM2> is: <RESULT>
print("Hi, {}, Multiplying {} and {} is {}".format(user_name, user_num1, user_num2, result))


#Q3: Converting code to use a while loop: (3 pts)



"""
Rewrite the guessing game using a while loop (code in pyScript08.py -- Guessing game that asks the user to guess 
                                              "What is the name of the computer that played on Jeopardy?")
You may need to use if statements in this solution.
You may need to use the break statement or the continue statement in this solution
Remember to mimic the print statements after each try exactly like the original code (therefore, 
remember to keep track of which try the guesser is on to output the appropriate response).

"""




"""Q4: Counting each of the vowels: (3 pts)
 
Using ONE for-loop, count the number of each of the vowels in a string (use the following: sentence = "are you suggesting coconuts migrate")
Display how many a’s, e’s, i’s, o’s, and u’s are in the sentence.
Q5: Length of all the words in a sentence (based on exercise in pyScript13.py) (3 pts)
 
Create a long sentence of words (assume NO punctuation).
Put the words into a list (Hint: How are the words separated?). Separating words can be done before the list comprehension.
Use a list comprehension to return each word along with the length of it. Use: (word, len(word)) in your list comprehension.
Finally, print out each word and its length (you may use a simple for-loop to do this), but sort by smallest size first (Hint: Search for a method that can sort a list. What do you have to do when you are trying to sort a list of tuples?)
Q6: Map-Filter-Reduce examples: (3 pts)
 
In the PowerPoint slides describing "higher-order functions" (02-Python - Map Filter Reduce.pdf) there are three examples: one illustrating the use of map, the next one illustrating the use of filter, and the last one illustrating the use of reduce. Rewrite these three examples without using the map(), filter(), and functools.reduce() functions.


"""