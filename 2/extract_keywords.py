# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:03:30 2019

@author: MO

use this program to get extract keywords
put this program with the program named 'input_data.py' when using it
"""

import input_data as ind
import jieba.analyse as ja
import pandas as pd
import numpy as np

#choose the data
def choose_data(s = str):
    if s == "发明":
        data = ind.data_inv()
    elif s == "外观":
        data = ind.data_appearance()
    elif s == "新型":
        data = ind.data_new()
    return data


#extract keywords

#get keywords   
def keywords(s = str):
    #data preparation
    a = choose_data(s)
    result = pd.DataFrame({'keywords' : list(np.zeros(50)),
                           'weighted' : list(np.zeros(50))})
    b = str(a.摘要)
    
    #return the 50 most weighted keywords
    i = 0
    for x, w in ja.textrank(b,topK=50,withWeight=True):
        #removes punctuation and individual characters 
        if len(x) == 1:
            break
        else:
            result.loc[i] = [x,w]
            i = i + 1
             
    return (result)

    
if __name__ == '__main__':
    choose_data()
    keywords()
    
    