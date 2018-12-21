import pickle
import networkx as nx


def generate_graph():
    adj_list = pickle.load(open("relationship"))
    
    ldict = adj_list
    lgraph = nx.DiGraph()
    for key in ldict :
        l = ldict.get(key)
        for i in range(0, len(l)) :
            lgraph.add_edge(key, l[i])

    return lgraph




if __name__ == '__main__':

    graph_mappings = pickle.load(open("graph_mapping"))
    cur_graph = generate_graph()
    all_nodes = cur_graph.nodes()
    success_nodes = set()


    for left_node, map_node in graph_mappings.iteritems():
        if left_node == map_node:
            success_nodes.add(left_node)
    error_nodes = set(all_nodes) - success_nodes



    success_nodes_degrees = cur_graph.degree(success_nodes)
    success_degrees = sum(success_nodes_degrees.values())

    error_nodes_degrees = cur_graph.degree(error_nodes)
    error_degrees = sum(error_nodes_degrees.values())
    print("Success rate is %s" % (success_degrees * 100.0/ (error_degrees+success_degrees)))
    print("Error rate is %s" % (error_degrees * 100.0 / (error_degrees + success_degrees)))


