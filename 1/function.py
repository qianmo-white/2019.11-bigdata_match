# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 00:24:52 2019

@author: MO

This program has some functions 
"""
import numpy as np
import re

#write the data to the flie
def write(filename = str, mylist = list):
    file = open(filename,'w',encoding = 'utf-8')
    for i in range(len(mylist)):
        s = mylist[i]
        file.write(s)      

#regular expressions determine numbers
pattern = re.compile('[0-9]+') 

def judge(s = str):
    match = pattern.findall(s)
    if match == []:
        return False
    else:
        return True

#people counting
def count_p(s = str):
    a = s.count(';') + 1
    return a
 
def norm(x):
    if np.logical_not(np.min(x),np.max(x)):
       x =  (x - np.min(x)) / (np.max(x) - np.min(x))
    x.fillna(value=1)
    return x   
    
if __name__ == '__main__':
    write()
    judge()
    count_p()
    norm()
    