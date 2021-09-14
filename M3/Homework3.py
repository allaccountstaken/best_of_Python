#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:29:17 2021
Name of activity:Homework Python I
Student name: Dmitry MIkhaylov
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

    if response == answer: # check if response matches the answer
        print("That is right!") 
        break # if True, break the loop after saying "Congrats!"
    else: # if False, then... 
        i = i + 1 # Increment the number of guesses used
        if i == 2:
            response = input("Sorry. Guess again: ") # if it's 2nd guess - 2 more to go
            continue
        elif i == 3:
            response = input("Sorry. One more guess: ") # if it's 3d guess - 1 more to go
            continue
        else:
            print("Sorry. No more guesses. The answer is " + answer + ".") # if more than 3, terminate the game


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
 
sentence = "Use this for now later it can be made even longer" # input sentence of variable length, no punctuations
words_list = sentence.split() # build a list of words by splitting a string
words_length = [(word, len(word)) for word in words_list] # build list of words and their lengths
# sselecting the second element (index=1) of the tuple
words_sorted = sorted(words_length, key=lambda words_length: words_length[1]) 
print(words_sorted) # print sorted results


#Q6: Map-Filter-Reduce examples: (3 pts)

def square_func(x): # a simple function for testing
    result = x * x    
    return result

def is_even(x): # a simple function for testing
    if x%2 ==0:
        result = True
    else:
        result = False
    return result

def sum(x, y): # a simple function for testing
    result = x + y
    return result




def my_map_func(apply_func, iter):
    """

    Parameters
    ----------
    apply_func : takes a 1-parameter function as the first argument.
    iter : takes an iterable type, i.e. list of numbers, to apply the input function to.

    Returns
    -------
    Output a list if elements to which the input function was applied.

    """

    result = [] # placeholder for output, empty for now
    
    for i in range(len(iter)):  # loop through all the elements of the input iterable
        result.append(apply_func(iter[i])) # apply the input function to every elements of the iterable, add to results
    
    return result # return the list of the results




def my_filter_func(apply_func, iter):
    """
    

    Parameters
    ----------
    apply_func : takes a function of a boolean type, i.e. function that returns True or False depending on a logic.
    iter : takes an iterable type, i.e. list of numbers, to apply the input function to.

    Returns
    -------
    Output a list of elements that meet the logical condition, i.e. function eveluated to True.

    """

    result = [] # placeholder for output, empty for now
    
    for i in range(len(iter)): # loop through all the elements of the input iterable
        if apply_func(iter[i]): # if input function eveluates to True on this iterable element, then ...
            result.append(iter[i]) # add this element to the outpult list
  
    return result #return the list of the results





def my_reduce_func(apply_func, iter):
    """
    

    Parameters
    ----------
    apply_func : takes a 2-argument function, i.e. sum(), and applys to elements of an iterable type.
    iter : takes an iterable type, i.e. list of numbers, to apply the input function to.

    Returns
    -------
    Output a single value hence the name reduce, i.e. iterable is reduced to a single value via functional transformation

    """

    result = 0 # placeholder for output, 0 for now
    for i in range(len(iter)): # loop through all the elements of the input iterable
        result = apply_func(result, iter[i]) # apply function to partial result ane the next element
    
    return result # return the final partial result, i.e. final result
        


# Testing for Q6:
numbers = [1, 2, 3, 4, 4, 5, 6, 7, 9]
my_map_func(square_func, numbers)
my_filter_func(is_even, numbers)
my_reduce_func(sum, [1, 2, 3])



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


# Testing for Q7
check1 = CHECKING("1234", 500, 0.5)
print(check1)
check1.withdraw(100)
print(check1)
check1.deposit(200)
print(check1)

