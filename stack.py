class Stack:
    def __init__(self):
        self._stack = []
    
    def push(self, item):
        """add item to top"""
        self._stack.append(item)
    
    def pop(self):
        """remove and return top item"""
        return self._stack.pop()

    def peek(self):
        """return top item without removing"""
        return self._stack[-1]

    def is_empty(self):
        """returns true if stack is empty"""
        return not self._stack
        