class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

    def __repr__(self):
        return f'Node {self.data} Next: {self.next}'

class LinkedList:

    def __init__(self, head):
        self.head = head
        self.tail = head
    
    def __repr__(self):
        return f"List Head: {self.head.data}, List Tail: {self.tail.data}"

    def add_to_end(self, node):
        self.tail.next = node
        self.tail = node

    def find_node(self, data_to_find):
        """find a specific node in a linked list"""

        current = self.head
        while current:

            if current.data == data_to_find:
                return current
            else:
                current = current.next

        return None

    def print_list(self):
        """print each node in list"""

        current = self.head
        while current:
            print(current)
            current = current.next


    def reverse_list(self):
        """reverse list without making a new list"""

        current = self.head
        new_next = None


        while current:

            forward = current.next
            current.next = new_next
            new_next = current
            current = forward

        self.head = new_next
        return new_next
            

n = Node(1)
n1 = Node(2)
n2 = Node(3)
n3 = Node(4)

ll = LinkedList(n)

ll.add_to_end(n1)
ll.add_to_end(n2)
ll.add_to_end(n3)
# print(ll.head)
# print(ll.reverse_list())
# print(ll.head)
ll.print_list()