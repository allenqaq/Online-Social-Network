'''
Created on Mar 3, 2017

@author: allen
'''

import networkx as nx
import matplotlib.pyplot as plt

# dicA = {'A' : ['B', 'C']}
# dicB = {'B' : ['C', 'A']}
# dicC = {'C' : ['A', 'B', 'G','D']}
# dicD = {'D' : ['E', 'F']}
# dicE = {'E' : ['D', 'F']}
# dicF = {'F' : ['D', 'E']}
# dicG = {'G' : ['K']}
# dicK = {'K' : ['G']}

dict = {'A' : ['B', 'C'], 'B' : ['C', 'A'], 'C' : ['A', 'B', 'G','D'], 'D' : ['E', 'F'], 'E' : ['D', 'F'], 'F' : ['D', 'E'], 'G' : ['K'], 'K' : ['G']}

for key in dict :
    l = dict.get(key)
    

G = nx.DiGraph()

# l = dicA.get('A')
# G.add_node('A')
# for i in range(0, len(l)) :
#     G.add_edge('A', l[i])
#     
# l = dicB.get('B')
# G.add_node('B')
# for i in range(0, len(l)) :
#     G.add_edge('B', l[i])
#     
# l = dicC.get('C')
# G.add_node('C')
# for i in range(0, len(l)) :
#     G.add_edge('C', l[i])
#     
# l = dicD.get('D')
# G.add_node('D')
# for i in range(0, len(l)) :
#     G.add_edge('D', l[i])
#     
# l = dicE.get('E')
# G.add_node('E')
# for i in range(0, len(l)) :
#     G.add_edge('E', l[i])
#     
# l = dicF.get('F')
# G.add_node('F')
# for i in range(0, len(l)) :
#     G.add_edge('F', l[i])
#     
# l = dicG.get('G')
# G.add_node('G')
# for i in range(0, len(l)) :
#     G.add_edge('G', l[i])
#     
# l = dicK.get('K')
# G.add_node('K')
# for i in range(0, len(l)) :
#     G.add_edge('K', l[i])
    
nx.draw(G)
plt.show()

G1 = G.to_undirected(reciprocal=True)

nx.draw(G1)
plt.show()

c = list(nx.k_clique_communities(G1, 2))
print(c)

print('Degree of A is : ',G.degree('A'))

print('Neighbors of A is : ', G.neighbors('A'))
num = len(G.neighbors('A'))
print('Neighbors account of A is : ', num)
