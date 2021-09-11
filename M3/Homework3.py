#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:29:17 2021
Homework Python
@author: dmitrymikhaylov
UVA ID: agp7dp
"""

#Q1: Dictionary basics: (2 pts)
 
# Create a dictionary of 10 key-value pairs. Choose a domain that interests you. What might you want to look up?
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



