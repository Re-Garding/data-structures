from collections import deque

class Node:


    def __init__(self, data, adjacent=[]):
        self.data = data
        self.adjacent = adjacent
    

    def __repr__(self):
        return f"<Node: {self.data}, Adjacent: {self.adjacent}>"


    def add_directional_adj(self, adj):
        """add adjacent nodes to node - single direction
            allows for multiples to be added at once"""
        self.add_adjacent.extend(adj)

    def add_mutual_adj(self, adj):
        """add mutual adjacent nodes"""
        
        self.adjacent.append(adj)
        adj.adjacent.append(self)



    def remove_adj(self, adj):
        """delete a node from adjacency"""

        self.adjacent.delete(adj)

    def is_connected(self, node):



class Graph:

    def __init__(self):
        self.nodes =  set()

    def a-star(self, node1, node2):
        """find lowest cost path between two nodes"""

def are_you_connected( node1, node2):
    """are two nodes connected"""

    seen = set([node1, node1.adjacent])
    to_see = deque(node1)

    while to_see:
        current = deque.popleft()
        
        if current.data = node2.data:
            return True
        seen.add(current)
        for node in current.adjacent:
            if node not in seen:
                to_see.append(node)
                seen.add(node)
    return False
