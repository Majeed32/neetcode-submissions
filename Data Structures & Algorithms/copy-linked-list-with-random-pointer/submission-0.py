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
        if not head:
            return head
        curr = head
        while curr:
            temp = curr.next
            node = Node(curr.val, temp)
            curr.next = node
            curr = temp
        curr = head
        while curr:
            temp = curr.next
            if curr.random:
                temp.random = curr.random.next
            curr = curr.next.next
        res = head.next
        copy = res
        curr = head
        while res.next:
            temp = res.next
            res.next = temp.next
            curr.next = temp
            res = res.next
            curr = curr.next
        return copy