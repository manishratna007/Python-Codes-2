# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 16:00:08 2021

@author: manis
"""

'''1.Load the dataset into a pandas dataframe. Name thevariable as “survey”.'''
import pandas as pd
survey=pd.read_excel(r'D:\Interview Prep\Applications\Dhruv Research\Sample Survey.xlsx',sheet_name='Data')

'''2.How many samples were collected on each day?'''
sample_each_day=survey['collection_date'].value_counts()
print(sample_each_day)

'''3.What proportion of the total respondents were agedless than 45?'''
survey['age']=survey['age'].astype(str)
survey["age"]=survey["age"].str.replace("24ko","24")
survey["age"]=survey["age"].astype(int)
df=survey[survey['age']<=45]
prop=len(df)/len(survey)*100
print(prop)

'''4.Create a new column in the dataframe “age_group”.This column should contain the age
group the respondent belongs to.  The age groups are18-25, 25-40, 40-55 and 55+. The
dataframe should look like this after the column creation:'''
bins = [18, 25, 40, 55,150]
labels = ['18-25', '25-40', '40-55', '55+']
survey['age_group'] = pd.cut(survey['age'], bins, labels = labels,include_lowest = True)
print(survey[['age','age_group']])

'''5.How many samples were collected for each age-group?Which age-group had the most samples'''

age_sample_each_day=survey['age_group'].value_counts()
survey['age_group'].value_counts().idxmax()

'''6.What proportion of the respondents had opted for theRJDparty in both the Vote_Now 
and the Past_Vote questions?'''

survey["Vote_Now"]=survey["Vote_Now"].astype(str)
survey["Past_Vote"]=survey["Past_Vote"].astype(str)
survey.dtypes
rjd=survey[(survey['Vote_Now']=='RJD') & (survey['Past_Vote']=='RJD')]
rjdSup=len(rjd)/len(survey)*100
print(rjdSup)

'''7. For each day of sample collection, determine the proportionof respondents who werefully 
satisfied with the performance of the CM. Soif there were a total of 1000 sampleson day 1 and
 300 out of those said they were fullysatisfied, then our answer for that daywould be 0.3.'''
satis= survey[survey['CM_satisfaction']=='Fully Satisfied']
satis1=satis['collection_date'].value_counts()
satis2=pd.concat([satis1,sample_each_day],axis=1) 
satis2.columns=["A","B"]
satis3=satis2['A']/satis2['B']*100
print(satis3) 


'''8. In a similar fashion create a day-wise proportionof respondents that 
opted fullydissatisfied with their MLA. Create a line plot ofthe result with 
date on x-axis andproportions on the y-axis'''
dissatis= survey[survey['CM_satisfaction']=='Fully Dissatisfied']
dissatis1=dissatis['collection_date'].value_counts()
dissatis2=pd.concat([dissatis1,sample_each_day],axis=1) 
dissatis2.columns=["A","B"]
dissatis3=dissatis2['A']/dissatis2['B']*100
print(dissatis3) 

dissatis4=pd.DataFrame(dissatis3,index=dissatis3.index)
print(dissatis4)
dissatis4.columns=['A']
dissatis4.index
dissatis4.plot.line()

'''9. Create a pivot-table (or crosstab) with index as Past_Vote,Column as
 Vote_Now andcell values as the count of samples.'''

cross=pd.crosstab(survey['Past_Vote'], survey['Vote_Now'])
print(cross)

'''10.Repeat the above question with the cell values asthe sum of “weight”.'''

sum_weight=pd.crosstab(survey['Past_Vote'], survey['Vote_Now'],values=survey['weight'],aggfunc=sum)
print(sum_weight)

'''11.Create a dataframe by performing a group by over age_groupand calculate 
the count oftotal samples under each age_group.'''

ageGrp=survey.groupby(['age_group']).count()
print(ageGrp['response_id'])

'''12.Create a dataframe by performing a group by over age_group and finding 
the count oftotal samples for each age_group that opted for theJD(U) party in
 Vote_Now.'''

jdu_sup=survey[survey['Vote_Now']=='JD(U)']
jduAgeGrp=jdu_sup.groupby(['age_group']).count()
print(jduAgeGrp['response_id'])

'''13. Join/Merge the two dataframes from questions 12 and 11 with the common
 column as age_group.'''
final=pd.merge(ageGrp['response_id'],jduAgeGrp['response_id'],on='age_group') 
final.columns=['Total Sample','JD(U) Supporters']
print(final)
