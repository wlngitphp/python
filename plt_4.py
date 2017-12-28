#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

food = pd.read_csv('../food_info.csv')
num_col = ['Water_(g)','Energ_Kcal','Lipid_Tot_(g)']
bar_height = food.loc[0,num_col].values
print(bar_height)
bar_posi = np.arange(3)+0.75
#print(bar_posi)
ax = plt.subplot()#画一个图
#ax.bar(bar_posi,bar_height ,0.3)#0.3表柱宽度竖形图
#ax.barh(bar_posi,bar_height ,0.3)#0.3表柱宽度横形图
ax.scatter(bar_posi,bar_height ,0.3)#0.3表柱宽度散点形图
plt.show()