#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 17:44:08 2021

@author: dmitrymikhaylov
"""


"""
1.   Prompt user for:   First name, Last name,  and Age. [Note: Feel free to be creative here if you like!] 
2.   After fetching First name, Last name, and Age, eliminate any whitespace from either the left-hand side 
or the right-hand side.
3.  After fetching First name, Last name, and Age, eliminate any whitespace from either the left-hand side 
or the right-hand side.
4. Concatenate the First name and the Last name into a single string so it looks like “Last-First” 
(with a dash separating the last and first names).
5. Create a dictionary and add this information to it where the name (“Last-First”) is the key and 
the age (an integer) is the value.
6. Simulate gathering information for four people. Your program should add each person’s information 
to the dictionary as described.
7. Print out the dictionary to a simple text file (e.g., “myOutput.txt”). 
"""

prompt_user = "Collecting info for 4 people. Please provide your first name, last name, and age"


first_name = input("What is your first name? (alphabetic input is expected)")
last_name = input("What is your last name? (alphabetic input is expected)")
age = int(input("How old are you? (numeric input is expected)"))

full_name = first_name+'-'+last_name
name_dict = {full_name:age}