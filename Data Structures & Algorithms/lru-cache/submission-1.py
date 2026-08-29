class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, Node):
        nxt, prev = Node.next, Node.prev
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
        curr_cache = Node(key, value)
        self.cache[key] = curr_cache
        self.insert(curr_cache)
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]