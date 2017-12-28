#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#fig = plt.figure()#draw area
#fig = plt.figure(figsize=(3,3))#指定宽高
#ax1 = fig.add_subplot(2,1,1)#画一个子图参数表示2,2表示2行2列，1表示第一个子图
ax2 = fig.add_subplot(2,1,2)
#ax3 = fig.add_subplot(2,2,4)
#print(np.random.randint(1,5,5))指定1,5的数字共5个
#print(np.arange(5))
#ax1.plot(np.random.randint(1,7,5), np.arange(5))
#ax2.plot(np.arange(4)*10,np.arange(4),c='red')#同一个图(ax2)指定线颜色
#ax2.plot(np.arange(6)*4,np.arange(6),c='blue')
fig.plot()
plt.show()