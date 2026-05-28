class Node:

    __slots__ = ["value", "next"]

    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, Node):
        self.next = Node

    def set_value(self):
        self.value
    
    def get_next(self):
        return self.next
    
    def get_value(self):
        return self.value