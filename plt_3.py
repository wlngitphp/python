#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

unrate = pd.read_csv('../UNRATE.csv')
#print(unrate)
fig = plt.figure(figsize = (10,6))
color = ['red','blue','green','orange','black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*10
    label = str(1948+i)
    subset = unrate[start_index:end_index]
    plt.plot(subset['DATE'],subset['VALUE'],c = color[i],label=label)
plt.xticks(rotation=45)
plt.legend(loc='best')#定位（best是plt自认为最好位置）
#print(help(plt.legend))
plt.show()