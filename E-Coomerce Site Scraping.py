# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 17:05:30 2021

@author: manis
"""
import pandas as pd
import selenium 
from selenium import webdriver as wb

''' open site '''

webD=wb.Chrome(r"C:\Users\manis\Downloads\Random Files\chromedriver_win32\chromedriver.exe")
webD.get('https://webscraper.io/test-sites/e-commerce/static')

'''click on location'''
clickobj1 = webD.find_element_by_xpath('//*[@id="side-menu"]/li[2]/a')
clickobj1.click()

'''click on location'''
clickobj2 = webD.find_element_by_xpath('//*[@id="side-menu"]/li[2]/ul/li[1]/a')
clickobj2.click()


listOfLinks=[]
condition = True

while condition:
    productInfoList=webD.find_elements_by_class_name('thumbnail')   
    for el in productInfoList:
        pp1=el.find_elements_by_tag_name('h4')[-1]
        pp2=pp1.find_element_by_tag_name('a')
        listOfLinks.append(pp2.get_property('href'))
    try:
        webD.find_elements_by_class_name('page-link')[-1].click() 
    except:
        condition = False


from tqdm import tqdm
alldetails=[]
for i in tqdm(listOfLinks):
    webD.get(i)
    nameOfProd=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]').text
    priceOfProd=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[1]').text
    description=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/p').text
    review=webD.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[3]/p').text
    tempDict={'nameOfProd':nameOfProd,'priceOfProd':priceOfProd,'description':description,'review':review,'linkofproduct':i}
    alldetails.append(tempDict)

df=pd.DataFrame(alldetails)
import os
os.chdir(r'D:\Interview Prep\Lectures\Python')

df.to_csv(r'D:\Interview Prep\Lectures\Python\1.csv')









