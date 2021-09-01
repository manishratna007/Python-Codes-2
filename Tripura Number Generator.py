# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 14:23:17 2021

@author: manis
"""
import pandas as pd
import numpy as np
import random
from random import shuffle

df=pd.read_excel(r'C:\Users\manis\Downloads\Work\Tripura\Tripura Mobile Datasets\TR-Vendor+Scraping-14995.xlsx',sheet_name="Vendor Only")

df['Min Num'].head
df['Max Num'].head
len(df['Min Num'])
len(df['Max Num'])

df['Min Num'][0]

sample=range(df['Min Num'][0],df['Max Num'][0])

sample_df=pd.DataFrame(range(df['Min Num'][0],df['Max Num'][0]),columns=['Mobile'])
len(sample)
sample_df.head
type(sample)

final_df=pd.DataFrame([])

for i in range(0,41):
    sample=pd.DataFrame(range(df['Min Num'][i],df['Max Num'][i]),columns=['Mobile'])
    final_df=final_df.append(sample)
    print(sample)
    
final_df.head
len(final_df)

final_unique=final_df.drop_duplicates()
len(final_unique)

final_unique_random= final_unique.sample(frac=1).reset_index(drop=True)

final_unique_random.to_csv(r'C:\Users\manis\Downloads\Work\Tripura\Tripura Mobile Datasets\TR-Vendor Only-4L -Series1-41.csv')

for i in range(0,25400888,950000):
    print(i)
    df1 = final_unique_random.iloc[i:i+950000]
    df1.to_csv('Tripura_numbers'+str(i)+'.csv',index=False)
    

import os
os.getcwd()
