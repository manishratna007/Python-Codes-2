# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 11:22:07 2021

@author: T.M.K
"""

'''in_file_path= r"C:\Users\T.M.K\Downloads\Output-13-03-2021\Checked"'''

import os

os.chdir(r"C:\Users\T.M.K\Downloads\Output-13-03-2021\Checked")

from docx2pdf import convert

convert(r"28_Chopra.docx")
convert(r"28_Chopra.docx", r"28_Chopra.pdf")

convert(r"C:\Users\T.M.K\Downloads\Output-13-03-2021\Checked")

