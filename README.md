# Online-Social-Network

Part 1: Crawling data
We have crawled the data from twitter. We use bfs to collect 225530 twitter users and make it two graphs . We use adjacency list to represent the edge and the result is stored in the file `relationship`.

Part 2: Implement S&P 09 Pape

(1): In the seed selection part, the implement is based on the posted version of seed selection. Loading the relationship file takes it as an input file. Then turn it into the python data structure dictionary.

    lgraph = nx.DiGraph()
    for key in ldict :
        l = ldict.get(key)
        for i in range(0, len(l)) :
            lgraph.add_edge(key, l[i])

(2): In the propagation part, the implement takes the pseudo-code of algorithm in the S&P 09 Paper. The basic idea is choosing a node from left graph, calculating the similarity scores of that node in the right graph, picking up the maximum one, reversing the process by starting with the maximum scores node and checking whether the first node and reverse maximum score node are the same nodes.

Here, little adjustment is adding into the algorithm. When calculating the node scores, adding a parameter that about the degree can make the algorithm work better.

skip = rgraph.in_degree(rnode[1]) - rgraph.in_degree(lnode)

skip is a degree check supposing 2 mapping mode degree differential is less than 3
                if skip > 3 or skip < -3 :
                    continue

The “skip” is the parameter control the similarity of the node score. Simple suppose is mode- supposing 2 mapping mode degree differential is less than 3. This process contributes accuracy of the calculation of the node scores.

(3): In the result part, the algorithm is successfully mapping 5231 out of 225530 and the mapping rate is 2.32%. Since two graph is the same, the mapping correctness is 100%.



From this result, the mapping  rate has only 2.32% for 2 reasons. The first is the data sources is not so suitable for the algorithm since the clique is only found one that with 3 nodes clique in 225530 nodes. 



The second is that the propagation is a simple loop for all nodes. When we update the mapping list, the unmapped nodes that has been processed before maybe could be mapped. The bigger mapping list, the bigger possible to be mapped.

Part 3: Improved Algorithm

I made improvement over two parts, both the seed selection stage and propagation stage.
For the seed selection part, the core algorithm remains the same. In the baseline algorithm, we change the k(the size of the clique) to find a successful mapping and only pick one k for mapping. In the improved algorithm, I try to start by making k = 10 then find the clique one by one to k = 3. See code
```
    for cur_k in range(10, 2, -1):
        one_map = find_k_clique_seed(lgraph, rgraph, cur_k, 0.01, lgraph_undirected, rgraph_undirected)
        if one_map:
            result_mappings.extend(one_map)
```
In this case, we can map as many cliques as we can instead of only finding clique with 1 k value.
Also, we make ε small enough, because we have known the two graphs we have collected are exactly the same.

For the second part of propagation, the basic idea is similar to the baseline algorithm but I have changed it to make successful in mapping and more efficient in running the code.
The details of propagation algorithm is shown as below

(1) . The algorithm takes as input the G(san).

(2). The algorithm takes as input the G(aux)

(3). The algorithm picks a mapped node v and v’ between G(san) and G(aux), and for each node v and v’ list all their

neighbours v(nbr), for each neighbour node v(nbr) we list its four attributes

	1’ List all v(nbr)’s neighbour nodes that are outcoming nodes and in the mapped nodes (between G(san) and G(aus)).
	2’ List all v(nbr)’s neighbour nodes that are incoming node and in the mapped nodes (between G(san) and G(aus))
	3’ Compute the number of the v(nbr)’s neighbour nodes that are outcoming nodes and NOT in the mapped nodes.
	4’ Compute the number of the nodes that are incoming nodes and NOT in the mapped nodes.
	
(4). Try to map all the neighbour nodes of v and neighbour nodes of v’ using similarity scores based on the four attributes.
	Similarity scores consists of four parts corresponding to four attributes.
	
	1’  1 - (the size of the common outcoming nodes in the mapped graph) /  (the maximum number of outcoming nodes)
	2’ 1 - (the size of the common incoming nodes in the mapped graph) /  (the maximum number of incoming nodes)
	3’ the absolute value of the difference between the number of outcoming nodes not in the mapped node of G(san) and G(aus) / the max value of previous two numbers
	4’ similar to 3’ , compute the nodes of incoming.
	See source code `improved_propagation.py` line
	If the similarity scores is lower, it is more likely that two nodes are matched.
	
 (5) Repeat step (3) and (4) using bfs until we have mapped the maximum nodes.

In the source code, I make more minor changes to the algorithm mainly to speed up.

Evaluation stage
There are 225530 nodes in our graph and two graphs are identical, the improved algorithm can map 98.35% of the nodes based on the success rate equation.
See source code evaluate.py for detail and run it to check the result


