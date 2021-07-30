# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:56:42 2021

@author: manis
"""
import pandas as pd
df=pd.read_excel(r'C:\Users\manis\Downloads\Work\UK Call Centre\Uttarakhand Data.xlsx')

df1l=pd.read_excel(r'C:\Users\manis\Downloads\Work\UK Call Centre\Uttarakhand Data_100k.xlsx')

df.head()

df=df['MOBILE']
len(df)

df1l.head()
df.head()

len(df1l)

type(df1l)
type(df)

df=pd.DataFrame(df)
type(df)

dfunique = pd.concat([df, df1l])
dfunique.shape
df_uniq_final=dfunique.drop_duplicates(keep=False)
df_uniq_final.shape
df_uniq_final.head()

df_random = df_uniq_final.sample(frac=1).reset_index(drop=True)
df_random.head()

df1=df_random.iloc[:100000,:]
df1.head()
df1.shape




