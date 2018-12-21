import pickle
import networkx as nx
import time



def generate_mappings():
    ori_mapping = pickle.load(open("clique_mapping"))
    res_mapping = {}
    for one_mapping in ori_mapping:
        for node, node_map in one_mapping.iteritems():
            if node not in res_mapping:
                res_mapping[node] = node_map
    return res_mapping


def generate_graph():
    adj_list = pickle.load(open("relationship"))
    
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
    return [lgraph, rgraph]



def calculate_score(cur_node, cur_graph, nodes_set):
    incoming_nodes = cur_graph.predecessors(cur_node)
    outcoming_nodes = cur_graph.successors(cur_node)    
    incoming_in_graph = set(nodes_set) & set(incoming_nodes)
    outcoming_in_graph = set(nodes_set) & set(outcoming_nodes)
    remain_incoming_len = len(incoming_nodes) - len(incoming_in_graph)
    remain_outcoming_len = len(outcoming_nodes) - len(outcoming_in_graph)
    return [incoming_in_graph, outcoming_in_graph, remain_incoming_len, remain_outcoming_len]


def left_right_score(left_score, right_score):
    first_score = 1 - len((set(left_score[0]) & set(right_score[0]))) / float(max(len(left_score[0]), len(right_score[0]))) if max(len(left_score[0]), len(right_score[0])) != 0 else 0
    second_score = 1 - len((set(left_score[1]) & set(right_score[1]))) / float(max(len(left_score[1]), len(right_score[1]))) if max(len(left_score[1]), len(right_score[1])) != 0 else 0
    third_score = abs(left_score[2] - right_score[2]) / float(max(left_score[2], right_score[2])) if max(left_score[2], right_score[2]) != 0 else 0
    fourth_score = abs(left_score[3] - right_score[3]) / float(max(left_score[3], right_score[3])) if max(left_score[3], right_score[3]) != 0 else 0

    return (first_score + second_score + third_score + fourth_score) / 4



 
def compare_score(left_scores, right_scores, graph_mappings):
    right_visited = set()
    if len(left_scores) != len(right_scores):
        return
    for left_node, left_score in left_scores.iteritems():
        min_score = 1
        match_node = None
        for right_node, right_score in right_scores.iteritems():
            if right_node in right_visited:
                continue
            cur_score = left_right_score(left_score, right_score)
            if cur_score < min_score:
                min_score = cur_score
                match_node = right_node
        right_visited.add(match_node)
        print("Map from %s -> %s, Total success num %s" % (left_node, match_node, len(graph_mappings)))
        graph_mappings[left_node] = match_node


def map_iter(lgraph, rgraph, graph_mappings, iter_times = 0, cur_nodes = None):
    cur_nodes = graph_mappings.keys() if iter_times == 0 else cur_nodes
    total_nodes = lgraph.number_of_nodes()
    while 1:
        next_nodes = []
        for cur_node in cur_nodes:     
            def _two_nodes(left_nodes, right_nodes, graph_mappings, lgraph, rgraph):
                left_scores, right_scores = {}, {}
                for left_node in left_nodes:
                    if left_node in graph_mappings:
                        continue
                    score = calculate_score(left_node, lgraph, graph_mappings)
                    left_scores[left_node] = score

                for right_node in right_nodes:
                    if right_node in graph_mappings.values():
                        continue
                    score = calculate_score(right_node, rgraph, set(graph_mappings.values()))
                    right_scores[right_node] = score
                compare_score(left_scores, right_scores, graph_mappings)


            left_incoming_nodes = lgraph.predecessors(cur_node)
            right_incoming_nodes = rgraph.predecessors(graph_mappings[cur_node])
            _two_nodes(left_incoming_nodes, right_incoming_nodes, graph_mappings, lgraph, rgraph)

            left_outcoming_nodes = lgraph.successors(cur_node)
            right_outcoming_nodes = rgraph.successors(graph_mappings[cur_node])
            _two_nodes(left_outcoming_nodes, right_outcoming_nodes, graph_mappings, lgraph, rgraph)

            next_nodes.extend(left_incoming_nodes+left_incoming_nodes)
            pickle.dump(graph_mappings, open("graph_mapping", "w"))
            print("--------")
            if iter_times == 0 and len(graph_mappings) > total_nodes / 3:
                return
        if iter_times != 0:
            return
        cur_nodes = next_nodes


def second_map(lgraph, rgraph, graph_mappings, all_nodes):
    while 1:
        remaining_nodes = all_nodes - set(graph_mappings)
        cur_nodes = []
        for remain_node in remaining_nodes:
            pre_nodes = lgraph.predecessors(remain_node)
            next_nodes = lgraph.successors(remain_node)
            for candidate in pre_nodes + next_nodes:
                if candidate in graph_mappings:
                    cur_nodes.append(candidate)
        map_iter(lgraph, rgraph, graph_mappings, iter_times=1, cur_nodes=cur_nodes)



if __name__ == "__main__":
    graph_mappings = generate_mappings()
    lgraph, rgraph = generate_graph()
    all_nodes = set(lgraph.nodes())
    map_iter(lgraph, rgraph, graph_mappings)
    second_map(lgraph, rgraph, graph_mappings, all_nodes)

