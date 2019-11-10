# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:18:00 2019

@author: MO

put this program with the table named '2.xlsx' when using it
use this program to get the data about the second problem
"""

import pandas as pd

data = pd.read_excel("2.xlsx")  

# get the invention about the patent

def data_inv():
    data_inv = []
    n = []
    for i in range(len(data)):
        if (data.专利类型[i].find("发明") != -1):
            n.append(i)
        else:
            continue
    data_inv = data.iloc[n,[1]]
    return data_inv
            
# get the appearance about the patent

def data_appearance():
    data_app = []
    n = []
    for i in range(len(data)):
        if (data.专利类型[i].find("外观") != -1):
            n.append(i)
        else:
            continue
    data_app = data.iloc[n,[1]]
    return data_app

# get the new type about the patent

def data_new():
    data_new = []
    n = []
    for i in range(len(data)):
        if (data.专利类型[i].find("新型") != -1):
            n.append(i)
        else:
            continue
    data_new = data.iloc[n,[1]]
    return data_new
    
if __name__ == '__main__':
    data_inv()
    data_appearance()
    data_new()
    
    