# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 11:13:41 2021

@author: manis
"""

'''Merge all excel files into one'''

import os
import pandas as pd
os.chdir(r'C:\Users\manis\Downloads\Gujarat Census')

files=os.listdir(r'C:\Users\manis\Downloads\Gujarat Census')

all=[]
df=[]
df = pd. DataFrame()
for file in files:
    if file. endswith('.xlsx'):
        df = df. append(pd. read_excel(file), ignore_index=True)    
    

    
df.to_csv(r'C:\Users\manis\Downloads\Gujarat Census\all.csv')
