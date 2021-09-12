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
rgb_colors_dict = { # This is a dictionary of 10 RGB colors
    "Black":(0,0,0), 
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

answer = "Watson"
print("Here is a guessing game. You get three tries.")
print("What is the name of the computer that played on Jeopardy?")
response = input("Type your answer here: ") # Ask user for input
i = 1 # Keep record of number of guesses used, start with 1

while i <= 3:

    if response == answer:
        print("That is right!")
        break
    else:
        i = i + 1 # Increment the number of guesses used
        if i == 2:
            response = input("Sorry. Guess again: ")
            continue
        elif i == 3:
            response = input("Sorry. One more guess: ")
            continue
        else:
            print("Sorry. No more guesses. The answer is " + answer + ".")


#Q4: Counting each of the vowels: (3 pts)
 
# Count the number of vowels in a longer string (sentence)
sentence = "are you suggesting coconuts migrate"
count = 0   # keep track of the vowels found
letters = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0} # initialize a dictionary to store counts of each desired letter

for letter in sentence: # loop through all the elements of the input string
    if letter in letters: # if letter matches the keys of desired letters...
        letters[letter] += 1 # then, increment the respective count

# Report back the original sentence and the counts of the desired letters
print("\"" + sentence + "\"")
print("These are the a’s, e’s, i’s, o’s, and u’s are in the sentence " + str(letters)) 




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




# Q7: Classes and Inheritance: (4 pts)


class ACCOUNT():
    
    
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance
    
    def __str__(self):
      result = "Account number {}\r\nBalance: {}".format(
          (self.accountNumber), (self.balance)
          )
      return result


class CHECKING(ACCOUNT):
    

    def __init__(self, accountNumber, balance, fee):
        ACCOUNT.__init__(self, accountNumber, balance)
        self.fee = fee
        
    def __str__(self):
      result = "Account number {}\r\nBalance: {}\r\nAccount type: Checking".format(
          (self.accountNumber), (self.balance)
          )
      return result

    def getFee(self):
        return self.fee

    def deposit(self, amount):
        self.balance = self.balance + amount


    def withdraw(self, amount):
        if amount+self.fee > self.balance: # checks the balance after transaction
            print("Insufficient funds!")
        else:
            self.balance = self.balance -  amount - self.fee


check1 = CHECKING("1234", 500, 0.5)
print(check1)
check1.withdraw(100)
print(check1)
check1.deposit(200)
print(check1)

