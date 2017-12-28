#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.txt',delimiter=',' ,dtype=str, skip_header=1)
# print(world_alcohol)
x = np.array([[1,2,3,3,4,5],[5,6,5,3,5,8],[5,6,7,8,5,8]])
# print(world_alcohol[2,4])
# print(x[:,1])
# print(x[0:1,0:3])
# b = np.array([4,6,10])
# print(b[b == 10])
# index = (x[:,3] == 3)
# print(index)
# print(index)
# print(x[index,:1])
# print(x.dtype)
# x = x.astype(float)
# print(x.dtype)
# print(x.min())
# print(x.sum(axis=1))#对行求和
# print(x.sum(axis=0))#对列求和
# print(np.arange(12))
# print(x.size)
# a = np.arange(12).reshape(3,4)
# print(a)
# print(np.zeros((2,3)))
# print(np.ones((3,4), dtype=np.int32))
# print(np.arange(10,30,5)) [10,15,20,25]
# print(np.random.random((2,3)))随机-1~1
# print(np.linspace(0,2*np.pi, 100))
# a = np.array([[2,3],[4,5]])
# b = np.array([[5,2],[2,7]])
# print(a*b)#对应位置相乘
# print(a.dot(b))#矩阵乘法
# print(np.dot(a,b))#矩阵乘法
# a = np.floor(10*np.random.random((2,3)))
# print(a.ravel())
# a = np.random.random((3,4))
# b = np.random.random((3,4))
# print(np.hstack((a,b)))
# print(np.vstack((a,b)))
# print(np.hsplit(a,2))切分为2份，
a = np.arange(12)
# b = a a,b 同一个
# b.shape = 2,6
# print(a.shape)
# c = a.view() a,b不一样但是改变c的值也会变
# c = a.copy() a,b不一样值改变c不影响a值

