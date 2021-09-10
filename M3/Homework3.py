#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 14:29:17 2021

@author: dmitrymikhaylov
"""
import sys

def lin_interaction():
    
    assert "linux" in sys.platform
    print("Do smng")
    
try: 
    lin_interaction()
except:
    print("this code did not execute")
        
        
        