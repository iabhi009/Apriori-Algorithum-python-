# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:36:51 2019

@author: iabhi
"""
import pandas as pd
import numpy as np

def rand(df):
    garray=np.array([])
    print(type(garray))
    print(df)
    print(df.shape)
    for x in df.columns:
        print(df[x])
    for row in range(df.shape[0]):
        print(row)
        garray=np.array([])
        
        for i in range(row+1,df.shape[0]):
            print(row+1, df.shape[0])
            x=np.array(df.iloc[i])
            garray=np.concatenate((garray, x))    
        print(garray)
#        d=[]
#        for j in range(0,row):
#            garray=[garray != df.iloc]
    
    
df=pd.DataFrame([['a','b'],['a','c'],['b','c']])
rand(df)