class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.next, self.prev = None, None
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, Node):
        prev, nxt = Node.prev, Node.next
        prev.next, nxt.prev = nxt, prev
    def insert(self, Node):
        prev, nxt = self.tail.prev, self.tail
        prev.next, nxt.prev = Node, Node
        Node.prev, Node.next = prev, nxt
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            delnode = self.head.next
            del self.cache[delnode.key]
            self.remove(delnode)
        
