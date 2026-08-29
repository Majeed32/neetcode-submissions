"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        while temp:
            nxt = temp.next
            temp.next = Node(temp.val, nxt)
            temp = nxt
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        dummy = Node(-1)
        curr = dummy
        old = head
        while old:
            copy = old.next
            curr.next = copy
            old.next = copy.next
            old = old.next
            curr = curr.next
        
        return dummy.next

        