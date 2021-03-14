# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:09:05 2021

@author: T.M.K
"""
"""!pip install reportlab"""

import os
os.chdir(r"C:\Users\T.M.K\Downloads\Ashish\Ashish")

import pandas as pd

import pdfkit as pdf

csv_file = 'Alipurduar _ Alipurduars.csv'

html_file = csv_file[:-3]+'html'

pdf_file = csv_file[:-3]+'pdf'

df = pd.read_csv(csv_file, sep=',')

df.to_html(html_file)

pdf.from_file(html_file, pdf_file)

