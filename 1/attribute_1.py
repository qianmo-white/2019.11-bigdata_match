# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:39:51 2019

@author: MO

Put this program with the table named '1.xlsx' when using it
Use this program to get the data about the first problem
"""

import pandas as pd

# get the status about the data
def data_status(use_cols = [2]):
    status = pd.read_excel("1.xlsx", usecols = use_cols)  
    status = status.values.tolist()
    return status
    
#get the area_code
def data_area_code(use_cols = [3]):    
    area_code = pd.read_excel("1.xlsx", usecols = use_cols)  
    area_code = area_code.values.tolist()
    return area_code
    
#get the organization
def data_organization(use_cols = [4]):      
    organization = pd.read_excel("1.xlsx", usecols = use_cols)  
    organization = organization.values.tolist()
    return organization

#get the genre
def data_genre(use_cols = [5]):    
    genre = pd.read_excel("1.xlsx", usecols = use_cols)  
    genre = genre.values.tolist()
    return genre

#get the inventor
def data_inventors(use_cols = [8]):
    inventor = pd.read_excel("1.xlsx", usecols = use_cols)  
    inventor = inventor.values.tolist()
    return inventor
       
#get the local
def data_local(use_cols = [10]):    
    local = pd.read_excel("1.xlsx", usecols = use_cols)  
    local = local.values.tolist()
    return local

#get the crouse 
def data_crouse(use_cols = [11]):    
    crouse = pd.read_excel("1.xlsx", usecols = use_cols)  
    crouse = crouse.values.tolist()
    return crouse

if __name__ == '__main__':
    data_status()
    data_area_code()
    data_genre()
    data_inventors()
    data_organization()
    data_local()    
    data_crouse()
        