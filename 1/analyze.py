# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:46:48 2019

@author: MO

Put this program with the 'data_clean.py' when using it
Use this program to finish the first problem 
"""

import data_clean as dc
import function as fun
import numpy as np
import pandas as pd

#area analyze and statistics

#data collection
area_data = []
organization_data = [] 
genre_data =[]
inventors_data = []

for i in range(len(dc.eff_data)):
    area_data.append((dc.eff_data[i])[0])
    organization_data.append((dc.eff_data[i])[1])
    inventors_data.append((dc.eff_data[i])[2])
    genre_data.append((dc.eff_data[i])[3])



#analyze the innovation index of area
area_statistics = np.unique(area_data)

#initialization  
orga_num = pd.DataFrame({'area'  : list(area_statistics),
                         'number_p' : list(np.zeros(len(area_statistics))), #the number of patents
                         'organization' : list(np.zeros(len(area_statistics))), #number of organization
                         'average' : list(np.zeros(len(area_statistics))),
                         'number_g' : list(np.zeros(len(area_statistics)))}) #number of patents for type of invention

# number of areas and number of organization counting  
for i in range(len(area_data)): 
    for j in range(len(area_statistics)):
        if area_data[i] == area_statistics[j]:
            orga_num.number_p[j] = orga_num.number_p[j] + 1
            orga_num.organization[j] = orga_num.organization[j] + 1
            
            if genre_data[i].find("发明") != -1:
                orga_num.number_g[j] = orga_num.number_g[j] + 1
        else:
            continue 

#average number of organization
for i in range(len(orga_num)):
    orga_num.average[i] = orga_num.number_p[i] / orga_num.organization[i]
    
#output the results as the .csv 
e_org = pd.DataFrame(index = orga_num.area,
                     data = {'average' : list(np.zeros(len(orga_num.area))),
                         'number_g' : list(np.zeros(len(orga_num.area)))})
    
for i in range(len(orga_num.area)): 
    e_org.average[i] = orga_num.average[i]
    e_org.number_g[i] = orga_num.number_g[i]

e_org.to_csv('result1_org.csv',encoding="utf_8_sig")  



#organization statistics
organization_statistics = np.unique(organization_data)

#initialization  
peo_num = pd.DataFrame({'inventors' : list(np.zeros(len(organization_statistics))), #number of inventors
                        'number_p' : list(np.zeros(len(organization_statistics))),#the number of patents
                        'organization' : list(np.zeros(len(organization_statistics))),
                        'average' : list(np.zeros(len(organization_statistics))),
                        'proportion' : list(np.zeros(len(organization_statistics))),
                        'number_g' : list(np.zeros(len(organization_statistics)))}) #number of patents for type of invention

# number of areas and number of organization counting      
for i in range(len(organization_data)): 
    for j in range(len(organization_statistics)):
        if organization_data[i] == organization_statistics[j]:
            peo_num.organization[j]= organization_statistics[j]
            peo_num.inventors[j] = fun.count_p(inventors_data[1])
            peo_num.number_p[j] = peo_num.number_p[j] + 1
            
            if genre_data[i].find("发明") != -1:
                peo_num.number_g[j] = peo_num.number_g[j] + 1
        else:
            continue 

#average number of inventors and the proportion for type in invention
for i in range(len(peo_num)):
    peo_num.average[i] = peo_num.number_p[i] / peo_num.inventors[i] 
    peo_num.proportion[i] = peo_num.number_g[i] / peo_num.number_p[i]

#output the results as the .csv 
e_peo = pd.DataFrame(index = peo_num.organization,
                     data = {'average' : list(np.zeros(len(peo_num.organization))),
                         'number_g' : list(np.zeros(len(peo_num.organization)))})
    
for i in range(len(peo_num.organization)): 
    e_peo.average[i] = peo_num.average[i]
    #e_org.average[i] = unicode(e_org.average[i], 'gbk')
    e_peo.number_g[i] = peo_num.number_g[i]

e_peo.to_csv('result1_peo.csv',encoding="utf_8_sig")  
