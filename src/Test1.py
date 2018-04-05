'''
Created on Feb 24, 2017

@author: allen
'''

# dic = {137 : [138,139,133]}
# 
# print(dic)
# 
# if 137 in dic :
#     print(dic[137][0])
#     

import networkx as nx
import matplotlib.pyplot as plt

# # regular graphy
# # generate a regular graph which has 20 nodes & each node has 3 neghbour nodes.
# RG = nx.random_graphs.random_regular_graph(3, 20)
# # the spectral layout
# pos = nx.spectral_layout(RG)
# # draw the regular graphy
# nx.draw(RG, pos, with_labels = False, node_size = 30)
# # plt.show()
# 
# l = ['a', 'b', 'c']
# print(len(l))

dict = {'A' : ['B', 'C'], 'B' : ['C', 'A'], 'C' : ['A', 'B', 'G','D'], 'D' : ['E', 'F'], 'E' : ['D', 'F'], 'F' : ['D', 'E'], 'G' : ['K'], 'K' : ['G']}
 
G = nx.DiGraph()
 
for key in dict :
    l = dict.get(key)
    for i in range(0, len(l)) :
        G.add_edge(key, l[i])
         
for i in G.nodes() :
    print(i)
     
print(G.out_edges('A'))
print(G.in_edges('A'))
li =  G.in_edges('A')
#  
# print(li[0][1])
# 
# l = []
# l[0] = [11, 12]
print(l)
scores = []
for i in range(G.number_of_nodes()) :
    scores.append(0)
    
print(G.number_of_nodes())

print('----------')

dict = {}

dict[999999] = [12342, 1234]

print(dict[999999])

print('----------')

list = []

list[1000000000000] = 100

print(list)
