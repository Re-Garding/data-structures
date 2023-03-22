""" a tree """

class Node:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __repr__(self):
        return f'Node {self.data}'

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_children(self):
        for child in self.children:
            print(child)

    def find_node_recurs(self, item):
        print(self.data)
        if self.data == item:
            return True
        elif self.children:
            return any([n.find_node_recurs(item) for n in self.children])
        else:
            return False



class Tree:
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return f'Tree Root {self.root}'

    def count_nodes(self):
        count = 0
        to_visit = [self.root]

        while to_visit:
            current = to_visit.pop()
            count += 1
            to_visit.extend(current.children)
        
        return count


    def is_node_in_tree(self, data):
        
        to_visit = [self.root]

        while to_visit:
            current = to_visit.pop()
            if current.data == data:
                return True
            else:
                to_visit.extend(current.children)
        return False
    





apple = Node('apple')
banana = Node('banana')
cherry = Node('cherry')
durian = Node('durian')
elderberry = Node('elderberry')
fig = Node('fig')
papaya = Node('papaya')
NT = Tree(apple)

apple.add_child(banana)
apple.add_child(cherry)
banana.add_child(durian)
durian.add_child(elderberry)
cherry.add_child(fig)
cherry.add_child(papaya)



#             apple
#              /   \
#         banana  cherry
#          /       /   \
#     durian     fig   papaya
#        /
# elderberry