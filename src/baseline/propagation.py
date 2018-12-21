'''
Created on Mar 5, 2017

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

# def stddev(lst):
#     """calculates standard deviation"""
#     sum = 0
#     mn = mean(lst)
#     for i in range(len(lst)) :
#         sum += pow((lst[i]-mn),2)
#     return sqrt(sum/len(lst)-1)

def eccenricity(items) :
    if not items :
        return 0;
    sd = np.std(items)
#     print(sd)
    if sd == 0 :
        return 0
    max1 = max(items)
    items.remove(max1)
    if len(items) != 0 :
        max2 = max(items)
    else :
        max2 = 0
#     print((max1 - max2) / sd)
    return (max1 - max2) / sd

def matchScores(lgraph, rgraph, mapping, lnode) :
#     print('match scores start')
    scores = {}
#     for i in lgraph.nodes():
#         scores[i] = 0
#     print(scores)
#     scores[lnode] = 0.1
    listIn1 = lgraph.in_edges(lnode)
    for lnbr in listIn1 :
        #lnbr is like (1111, 1112)
        if lnbr[0] not in mapping[0].keys() :
            continue
        rnbr = mapping[0][lnbr[0]]
        listOut1 = rgraph.out_edges(rnbr)
        for rnode in listOut1 :
            #rnode is like (1111, 1112)
#             if rnode[1] in mapping[0].keys() or rgraph.in_degree(rnode[1]) > 100 or rgraph.in_degree(rnode[1]) == 1:
            if rnode[1] in mapping[0].keys() :
                continue
            else :
                skip = rgraph.in_degree(rnode[1]) - rgraph.in_degree(lnode)
                # skip is a degree check supposing 2 mapping mode degree differential is less than 3
                if skip > 3 or skip < -3 :
                    continue
                elif rnode[1] in scores.keys() :
                    scores[rnode[1]] += 1 / sqrt(rgraph.in_degree(rnode[1]))
                else :
                    scores[rnode[1]] = 1 / sqrt(rgraph.in_degree(rnode[1]))
                
                
    listOut2 = lgraph.out_edges(lnode)
    for lnbr in listOut2 :
        #lnbr is like (1111, 1112)
        if lnbr[1] not in mapping[0].keys() :
            continue
        rnbr = mapping[0][lnbr[1]]
        listIn2 = rgraph.in_edges(rnbr)
        for rnode in listIn2 :
            #rnode is like (1111, 1112)
#             if rnode[0] in mapping[0].keys() or rgraph.out_degree(rnode[0]) > 100 or rgraph.out_degree(rnode[0]) == 1:
            if rnode[0] in mapping[0].keys() :   
                continue
            else :
                skip = rgraph.out_degree(rnode[0]) - rgraph.out_degree(lnode)
                # skip is a degree check supposing 2 mapping mode degree differential is less than 3
                if skip > 3 or skip < -3 :
                    continue
                if rnode[0] in scores.keys() :
                    scores[rnode[0]] += 1 / sqrt(rgraph.out_degree(rnode[0]))
                else :
                    scores[rnode[0]] = 1 / sqrt(rgraph.out_degree(rnode[0]))
                    
#     if lnode in scores.keys() and scores[lnode] != 0 :
#         print("lnode :"),
#         print(lnode)
#         print("shoule be scores : ")
#         print(scores[lnode])
#         print("max id is :"),
#         print(max(scores.items(), key=lambda x: x[1])[0])
#         print(max(scores.values()))
#         print(scores)

# #         for (k,v) in scores.items() :
# #             if v == max(scores.values()) :
# #                 print(k),
# #         print
#         print("--------------------------------------")
    return scores

def propagationStep(lgraph, rgraph, mapping) :
    scores = {}
    for lnode in lgraph.nodes() :
        if lnode in mapping[0].keys() :
            continue
        scores[lnode] = matchScores(lgraph, rgraph, mapping, lnode)
#         print(scores[lnode])
        if eccenricity(scores[lnode].values()) < 0.01 :
            # 0.01 is theta, a parameter that controls the tradeoff between the yield and the accuracy.
            continue
        rnode = max(scores[lnode].items(), key=lambda x: x[1])[0]
        scores[rnode] = matchScores(rgraph, lgraph, mapping, rnode)
        # no need to invert mapping
        if eccenricity(scores[rnode].values()) < 0.01 :
            # 0.01 is theta, a parameter that controls the tradeoff between the yield and the accuracy.
            continue
        
        reverse_match = max(scores[rnode].items(), key=lambda x: x[1])[0]
        print("reverse_match :"),
        print(reverse_match)
        print("lnode :"),
        print(lnode)
#         print(scores[rnode][reverse_match])
#         print(scores[rnode][lnode])
        print("======================================")
        if reverse_match != lnode :
            continue
        else :
            mapping[0][lnode] = rnode
