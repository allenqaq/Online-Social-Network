'''
Created on Mar 5, 2017

@author: allen
'''

import networkx as nx
import matplotlib.pyplot as plt

dict = {'A' : ['B', 'C'], 'B' : ['C', 'A'], 'C' : ['A', 'B', 'G','D'], 'D' : ['E', 'F'], 'E' : ['D', 'F'], 'F' : ['D', 'E'], 'G' : ['K'], 'K' : ['G']}

G = nx.DiGraph()

for key in dict :
    l = dict.get(key)
    for i in range(0, len(l)) :
        G.add_edge(key, l[i])
        
print(G.nodes())
        
# nx.draw(G)
# plt.show()
#  
# G1 = G.to_undirected(reciprocal=True)
#  
# nx.draw(G1)
# plt.show()

# c = list(nx.k_clique_communities(G1, 2))
# for i in range(len(c)) :
#     for t in c[i] :
#         print(t), 
# 
# 
# print('Degree of A is : ',G.degree('A'))
# 
# print('Neighbors of A is : ', G.neighbors('A'))
# num = len(G.neighbors('A'))
# print('Neighbors account of A is : ', num)