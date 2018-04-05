'''
Created on Mar 2, 2017

@author: allen
'''

import networkx as nx
import matplotlib.pyplot as plt

dic1 = {137 : [217, 139,138]}
dic2 = {138 : [137, 139]}
dic3 = {139 : [137, 138, 213]}
dic4 = {216 : [138]}

G=nx.DiGraph() 
# G=nx.Graph() 

G.add_node(137)
G.add_node(138)
G.add_node(139)
G.add_node(213)
G.add_node(217)
G.add_node(216)
G.add_node(218)

G.add_edge(137, 138)
G.add_edge(137, 139)
G.add_edge(137, 217)
G.add_edge(138, 137)
G.add_edge(138, 139)
G.add_edge(139, 138)
G.add_edge(139, 137)
G.add_edge(139, 213)
G.add_edge(216, 138)
G.add_edge(213, 218)
G.add_edge(218, 213)

G1 = G.to_undirected(reciprocal=True)

# '''
# the spectral layout
# pos = nx.spectral_layout(G1)
# draw the regular graphy
# nx.draw(G1)
# plt.show()
# '''

# c = list(nx.k_clique_communities(G1, 3))
# print(c)
c = list(nx.k_clique_communities(G1, 2))
print(c)
print(G.degree(138))
# l = G.edges()
# print(l)

num = len(G.neighbors(137))
print(num)

