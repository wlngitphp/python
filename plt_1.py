#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('UNRATE.csv')
#unrate['DATE'] = pd.to_datetime(unrate['DATE'])
#print(unrate['DATE'])
#print(unrate.head(12))
draw = unrate[:12]
#print(draw)
plt.plot(draw['DATE'], draw['VALUE'])
plt.xticks(rotation=90)#对x值显示转换角度
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends')
plt.show()