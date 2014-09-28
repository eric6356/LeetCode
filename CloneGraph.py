# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
        def addToDict(self, node_dict, node):
            if node.label in node_dict:
                return False
            nb_list = list()
            for nb in node.neighbors:
                nb_list.append(nb.label)
            node_dict[node.label] = nb_list
            for nb in node.neighbors:
                if not nb.label in node_dict:
                    self.addToDict(node_dict, nb)
            return True
        # @param node, a undirected graph node
        # @return a undirected graph node
        def cloneGraph(self, node):
            node_dict = dict()
            point_dict = dict()
            self.addToDict(node_dict, node)
            for key in node_dict:
                point_dict[key] = UndirectedGraphNode(key)
            for key in node_dict:
                for nb in node_dict[key]:
                    point_dict[key].neighbor.append(point_dict[nb])
            return point_dict[node.label]

