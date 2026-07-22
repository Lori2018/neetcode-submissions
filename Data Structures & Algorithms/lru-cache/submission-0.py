from collections import defaultdict, deque

class Node:
    def __init__(self, key, value):
        self.key = key # value
        self.value = value # value
        self.next = None
        self.prev = None

class LRUCache:
    # use linkedlist and keep track of a count of how many
    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.count = 0
        self.head = None
        self.tail = None


    def nodeAccessed(self, node):
        if node == self.tail:
            return
        prev = node.prev # none
        next = node.next # (2, 2)
        # node -> next
        if prev:
            prev.next = next
        if next: # next.prev = None
            next.prev = prev 
        if next == self.tail: 
            next.next = node
        node.next = None 
        node.prev = self.tail # node.prev = next
        if self.head == node and next: # self.head = next
            self.head = next
        if self.tail:
            self.tail.next = node
        self.tail = node


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            node = self.dict[key]
            self.nodeAccessed(node)
            return node.value
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict: 
            node = self.dict[key]
            node.value = value 
            self.nodeAccessed(node)
            return

        if self.count == self.capacity:
            if self.head.next: 
                self.head.next.prev = None
            del self.dict[self.head.key]
            self.head = self.head.next
            self.count -= 1

        # make node 
        node = Node(key, value)
        # add to dict
        self.dict[key] = node
        # append to linkedlist
        if not self.head:
            self.head = node 
            self.tail = node
        else: 
            self.tail.next = node 
            node.prev = self.tail
            self.tail = node
        self.count += 1
