#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:42:43 2017

@author: user
"""
import pandas
food_info = pandas.read_csv("food_info.csv")
#print(type(food_info))
#print(food_info.dtypes)
#print(help(pandas.read_csv))
#print(food_info.head(3))
#print(food_info.columns)
#print(food_info.shape)
#print(food_info.loc[0])
#print(food_info.loc[3:6])
#print(food_info['NDB_No'][6])
#print(food_info.columns.tolist())
#print(food_info['Iron_(mg)']/1000)
#print(food_info['Iron_(mg)'].max())
food_info.sort_values('NDB_No', inplace=True,ascending=False)
print(food_info['NDB_No'])