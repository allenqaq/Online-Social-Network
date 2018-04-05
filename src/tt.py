'''
Created on Mar 17, 2017

@author: allen
'''

import networkx as nx
from math import sqrt
import numpy as np
# def mean(lst):
#     """calculates mean"""
#     sum = 0
#     for i in range(len(lst)):
#         sum += lst[i]
#     return (sum / len(lst))
# 
# def stddev(lst):
#     """calculates standard deviation"""
#     sum = 0
#     mn = mean(lst)
#     for i in range(len(lst)) :
#         sum += pow((lst[i]-mn),2)
#     return sqrt(sum/len(lst)-1)

# def eccenricity(items) :
#     sd = np.std(items)
#     max1 = max(items)
#     l = items.remove(max1)
#     max2 = max(l)
#     return (max1 - max2) / sd

# print(eccenricity([1, 1, 1, 2, 2]))
# items = [1, 1, 1, 2, 2]
# max1 = max(items)
# print(max1)
# items.remove(max1)
# l = items
# print(l)
# max2 = max(l)

dict = {}

dict[100] = {}
dict[100][12] = 13
dict[100][13] = 12
dict[100][14] = 122
dict[100][15] = 21
dict[100][16] = 122
dict[100][17] = 1
dict[100][18] = 123
dict[100][19] = 10
# print(dict)

# dict[100][12] += 2

# print(dict[100][12])

# print(dict[100].values())

# print(max(dict[100].items(), key=lambda x: x[1])[0])

# def eccenricity(items) :
#     sd = np.std(items)
#     if sd == 0 :
#         return 0
#     print(sd)
#     max1 = max(items)
#     print(max1)
#     items.remove(max1)
#     if len(items) != 0 :
#         max2 = max(items)
#         print(max2)
#     else :
#         max2 = 0
#     print((max1 - max2) / sd)
#     return (max1 - max2) / sd
# 
# print(eccenricity(dict[100].values()))

scores = {}

# for i in range(10) :
#     scores[i] = 0
    
for i in range(10) :
    if i in scores.keys() :
        scores[i] += 9
    else :
        scores[i] = 9
    
print(scores)