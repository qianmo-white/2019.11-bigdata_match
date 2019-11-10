# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:50:41 2019

@author: MO

use this program to analyze the second problem
put this program with the program named 'extract_kewords.py' when using it
"""

import extract_keywords as ek

#patents for inventions
result_i = ek.keywords('发明')
#give up the data we don't need
for i in range(1,len(result_i)):
    if(result_i.iloc[i][0] == 0):
        result_inv = result_i.drop(result_i.index[range(i,len(result_i))],inplace=True)
        break
result_inv = result_i

#output the result        
result_inv.to_csv('result2_inv.csv',encoding="utf_8_sig")  


#patents for appearance
result_a = ek.keywords('外观')
#give up the data we don't need
for i in range(len(result_a)):
    if(result_a.iloc[i][0] == 0):
        result_app = result_a.drop(result_a.index[range(i,len(result_a))],inplace=True)
        break
result_app = result_a
   
#output the result   
result_app.to_csv('result2_app.csv',encoding="utf_8_sig")  


#patents for new-type
result_n = ek.keywords('新型')
#give up the data we don't need
for i in range(1,len(result_n)):
    if(result_i.iloc[i][0] == 0):
        result_new = result_n.drop(result_n.index[range(i,len(result_n))],inplace=True)
        break
result_new = result_n
 
#output the result     
result_new.to_csv('result2_new.csv',encoding="utf_8_sig")  
