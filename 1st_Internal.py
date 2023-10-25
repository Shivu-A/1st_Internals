# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd 
import numpy as np
data={'Chemistry':[67,90,60,32,72,45,60,98],
      'Physics':[45,92,72,92,72,34,72,45]}
df=pd.DataFrame(data,index=['Shivani','Akshay','Manjula','Shalini','Karthik','bhat','Chan','james'])
print(df)

print("Sum of each subject")
print(df.sum())
# OR
t_chem=df['Chemistry'].sum()
t_phy=df['Physics'].sum()
print(t_chem)
print(t_phy)

print("\nAverage of Chemistry")
aver_Chem=df['Chemistry'].mean()
print(aver_Chem)

print('\nMean marks')
mean_marks=df.mean()
print(mean_marks)



