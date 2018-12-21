'''
Created on Mar 5, 2017

@author: allen
'''

import time
import networkx as nx
import pickle
import propagation

def __find_k_cliques(G, k):
    rcl = nx.find_cliques_recursive(G)
    k_cliques_list = []
    while True:
        edge_list = []
        try:
            clique_list = next(rcl)
            if len(clique_list) != k:
                continue

            else:
                for i in range(len(clique_list)):
                    for j in range(i+1, len(clique_list)):
                        edge_list.append(G.has_edge(clique_list[i], clique_list[j]))
                        edge_list.append(G.has_edge(clique_list[j], clique_list[i]))

                if all( has_edge is True for has_edge in edge_list):
                    k_cliques_list.append(clique_list)

        except StopIteration:
            break

    if len(k_cliques_list) == 0:
        return None

    else:
        return k_cliques_list

def __calc_node_cnc(G_undirected, target_node, k_clique):
    sum_cnc = 0

    for node in k_clique:
        if target_node != node:
            sum_cnc += len(sorted(nx.common_neighbors(G_undirected, target_node, node))) - len(k_clique) + 2

    return float(sum_cnc)



def find_k_clique_seed(lgraph, rgraph, k, e):

    """Compute the k-clique seed selection
    This function is implemented based on NetworkX, please install it first!!!
    Args:
        lgraph is the left graph generated using NetworkX
        rgraph is the right graph generated using NetworkX
        k is the number of k-clique
        e is the threshold (epsilon)
    Returns:
        The list of mappings of seeds
    """

    lgraph_k_clqs = __find_k_cliques(lgraph, k)
    rgraph_k_clqs = __find_k_cliques(rgraph, k)
    print(rgraph_k_clqs)
    print(lgraph_k_clqs)
    lgraph_undirected = lgraph.to_undirected()
    rgraph_undirected = rgraph.to_undirected()

    ## mapping from lgraph to rgraph

    seed_mappings = []
    pre_time = time.time()
    if not lgraph_k_clqs or not rgraph_k_clqs:
        print 'No k-cliques have been found'
        return
    l_visited_index = set()
    r_visited_index = set()
    for left_index, lgraph_k_clq in enumerate(lgraph_k_clqs):
        for right_index, rgraph_k_clq in enumerate(rgraph_k_clqs):
            seed_mapping = {}
            if left_index in l_visited_index or right_index in r_visited_index:
                continue
            for lnode in lgraph_k_clq:
                for rnode in rgraph_k_clq:
                    lnode_cnc = __calc_node_cnc(lgraph_undirected, lnode, lgraph_k_clq)
                    rnode_cnc = __calc_node_cnc(rgraph_undirected, rnode, rgraph_k_clq)
                    lnode_degree = float(lgraph.degree(lnode))
                    rnode_degree = float(rgraph.degree(rnode))
                    if (1-e <= (lnode_cnc/rnode_cnc) <= 1+e) and (1-e <= (lnode_degree/rnode_degree) <= 1+e):
                        seed_mapping[lnode] = rnode
            # print("left:%s, right:%s. seed:%s" % (lgraph_k_clq[0], rgraph_k_clq[1], seed_mapping))
            if len(seed_mapping) == k:
                seed_mappings.append(seed_mapping)
                l_visited_index.add(left_index)
                r_visited_index.add(right_index)
                break

    return seed_mappings






'''An Example of how to use the function'''
if __name__ == '__main__':
    
    
    adj_list = pickle.load(open("relationship"))
#     adj_list = {1 : [2, 3, 7], 2 : [1, 3, 4, 7], 3 : [1, 2, 7, 5], 5 : [3, 6], 6 : [5], 7 : [1, 2, 3], 4 : [2]}
    ldict = adj_list
    rdict = adj_list
    
    lgraph = nx.DiGraph()
    rgraph = nx.DiGraph()
   
    for key in ldict :
        l = ldict.get(key)
        for i in range(0, len(l)) :
            lgraph.add_edge(key, l[i])
            
    for key in rdict :
        r = rdict.get(key)
        for i in range(0, len(r)) :
            rgraph.add_edge(key, r[i])

    mapping = find_k_clique_seed(lgraph, rgraph, k=3, e=0.01)
    print(mapping)
    if  mapping :
        propagation.propagationStep(lgraph, rgraph, mapping)
#         print(mapping)

    output = open('graph_mapping', 'wb')
    pickle.dump(mapping, output)
    output.close()
    
#     pkl_file = open('graph_mapping', 'rb')
#     data1 = pickle.load(pkl_file)
#     print(data1)
    
    print("***************************************")
    print("***************************************")
    print("***************************************")
    
    mapping_len = len(mapping[0])
    data_len = len(lgraph.nodes())
    
    print("number of mapping nodes ="),
    print(mapping_len)
    
    print("number of all nodes ="),
    print(data_len)
    
    mapping_rate = mapping_len * 100.0 / data_len
    print("mapping rate ="),
    print(mapping_rate)
    
    sum = 0
    for i in mapping[0] :
        if i == mapping[0][i] :
            sum = sum + 1
            
    correct_rate = sum * 100.0 / mapping_len
    print("correct rate ="),
    print(correct_rate)