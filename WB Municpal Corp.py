# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 12:58:39 2021

@author: manis
"""
import os
import pandas as pd

entries = os.listdir(r'C:\Users\manis\Downloads\Round 1\Round 1 - Copy\2017')
os.chdir(r'C:\Users\manis\Downloads\Round 1\Round 1 - Copy\2017')


for i in entries:
    try:
        df = pd.read_html(i)
        df1 = df[0]
        df1.ffill(axis = 0,inplace = True)
        df1['filename'] = os.path.basename(i)
        df1.to_csv(i+".csv",index=False)
    except:
        pass    
