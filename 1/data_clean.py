# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 15:12:39 2019

@author: MO

Put this program with the 'attribute_1.py' and 'function.py' when using it

Data cleaning
Foreign patents and unlicensed successful patents need to be removed
"""

import re
import numpy as np
import function as fun
import attribute_1 as attr

# all kinds of status
status = attr.data_status()
status_1 = np.unique(status)
#fun.write("stauts.txt",status) # print the status

# find the patent we need
patent_list = []

for i in range(len(status)):
    s = str(status[i])
    if s.find("授权") != -1:
        patent_list.append(i)
       
#effective data 
data = attr.data_status(use_cols=[2,3,4,5,8])        
eff_data = []
n = 0
for i in range(len(status)):
    s = str((data[i])[1])
    #determine location
    flag = fun.judge(s) or (s.find("CN") != -1)        
    s = data[i]
    if  (re.match("授权",s[0]) != None) and flag:
        eff_data.append(data[i])
        eff_data[n].remove("授权")
        n = n + 1
    else:
        continue
        