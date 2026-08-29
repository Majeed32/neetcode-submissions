class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-2, -2)
        self.head.next, self.tail.prev = self.tail, self.head

    def insert(self, node):
        prev_node = self.tail.prev
        node.next, node.prev = self.tail, prev_node
        self.tail.prev, prev_node.next = node, node
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        return node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.remove(self.map[key])
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.remove(self.map[key])
            node.val = value
            self.insert(node)
            self.map[key] = node
        else:
            node = Node(key, value)
            if len(self.map) == self.capacity:
                old =self.remove(self.head.next)
                del self.map[old.key]
            self.insert(node)
            self.map[key] = node

        
