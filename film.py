import numpy as np
import pandas as pd
from pandas import Series

fandango_score_comparison = pd.read_csv('fandango_score_comparison.csv')
#print(type(fandango_score_comparison))
#print(film)
#print(fandango_score_comparison.columns)
film = fandango_score_comparison['FILM']
#print(film)
scores = fandango_score_comparison['Metacritic_norm_round']
#print(film)
dianyin_values = film.values
rt_scores = scores.values
#print(type(dianyin_values))
#print(dianyin_values)
series_custom = Series(rt_scores,index=film)
#print(series_custom)
b = sorted(series_custom)
#print(b)
a = series_custom[['The Man From U.N.C.L.E. (2015)']]
#print(a)
c = fandango_score_comparison.set_index('FILM',drop=False)
#print(c)
print(c.loc['Cinderella (2015)'])