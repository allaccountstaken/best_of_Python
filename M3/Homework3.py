#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:29:17 2021
Homework Python I
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
fav_colors = ["Black", "White", "Red"] # Define 3 keys
[rgb_colors_dict.get(color) for color in fav_colors] # Pull values for those keys in a list comprehension 


# Alternatively, one can form a string in a for loop
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



#Q4: Counting each of the vowels: (3 pts)
 
"""
Using ONE for-loop, count the number of each of the vowels in a string (use the following: sentence = 
                                                                        "are you suggesting coconuts migrate")
Display how many a’s, e’s, i’s, o’s, and u’s are in the sentence.
"""




#Q5: Length of all the words in a sentence (based on exercise in pyScript13.py) (3 pts)
 
"""
Create a long sentence of words (assume NO punctuation).
Put the words into a list (Hint: How are the words separated?). Separating words can be done before the list comprehension.
Use a list comprehension to return each word along with the length of it. Use: (word, len(word)) in your list comprehension.
Finally, print out each word and its length (you may use a simple for-loop to do this), but sort by smallest size first 
(Hint: Search for a method that can sort a list. What do you have to do when you are trying to sort a list of tuples?)
"""


#Q6: Map-Filter-Reduce examples: (3 pts)
 
"""
In the PowerPoint slides describing "higher-order functions" (02-Python - Map Filter Reduce.pdf) 
there are three examples: one illustrating the use of map, the next one illustrating the use of filter, 
and the last one illustrating the use of reduce. Rewrite these three examples without using the map(), filter(), 
and functools.reduce() functions.

"""






"""
Q7: Classes and Inheritance: (4 pts)
 
Create a base class called ACCOUNT.
Account should have the following attributes: accountNumber and balance, which should be correctly initialized in the constructor (_ _init_ _) method for the class.
Create a to-string (_ _str_ _) method that prints “Account number 1234” on one line and “Balance: 2000” on the next line (example with account number of 1234 and balance of 2000).
Create another class called CHECKING. This class should inherit from the Account class. Therefore, the Checking class is the derived class.
In addition to the accountNumber and balance attributes, the Checking class has a fee attribute (that is used when withdrawing money from the Checking account). Initialize all variables correctly in the constructor (_ _init_ _) method.
Create a to-string method (_ _str_ _) that is identical to the two-line to-string method of the Account class, but has an additional header (a new first line): "Account type: Checking". Therefore, the to-string method of this class should produce a three-line output.
Add a method getFee(self) that returns the fee attribute (remember to use: self.fee).
Add a method deposit(self, amount) that adds the "amount" to the balance. It doesn't produce any output or return anything.
Add a method withdraw(self, amount) that does the following: (1) checks to see if the amount to withdraw + fee is greater than the balance; if so, display a message "Insufficient funds!", (2) otherwise, adjust the balance so that the amount AND the fee are subtracted. (Remember when you make a withdrawal, there is a fee involved that also needs to be subtracted from the balance. -- Example: Balance is $500. If you want to withdraw $100, and if the fee is $10, the method checks 110 is not greater than 500, so the resulting balance will be 500 - 100 - 10, so balance = $390.)
To test this out: (1) create an instance of the Checking class (call it check1) with account number 1234 and a balance of 500 with a fee of 0.50, (2) print check1 out, (2) withdraw $100, (4) print check1 out, (5) deposit $200, (6) print check1 out. See example below.
"""



