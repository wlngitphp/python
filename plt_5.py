#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt 

review = pd.read_csv('../fandango_score_comparison.csv')
cols = ['FILM','RT_user_norm_round','Metacritic_user_norm_round','IMDB_norm','Fandango_Ratingvalue']
norm_re = review[cols]
#print(norm_re[:5])
fand_dis = norm_re['Fandango_Ratingvalue'].value_counts()
print(fand_dis)
fand_dis = fand_dis.sort_index()
#print(fand_dis)
imdb_dis = norm_re['IMDB_norm'].value_counts()
imdb_dis = imdb_dis.sort_index()
ax = plt.subplot()
#ax.hist(norm_re['Fandango_Ratingvalue'])
#ax.hist(norm_re['Fandango_Ratingvalue'],bins=21)
ax.hist(norm_re['Fandango_Ratingvalue'],range=(4,5),bins=20)#x区间内的值(4,5)z