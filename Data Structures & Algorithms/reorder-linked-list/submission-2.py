# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(node):
            prev = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            return prev
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        curr = head
        for _ in range((length//2)-1):
            curr = curr.next
        next_node = curr.next
        curr.next = None
        half = reverse(next_node)
        curr = head
        while curr and half:
            tmp = curr.next
            nxt = half.next
            curr.next = half
            if tmp:
                half.next = tmp
                curr = tmp
            else:
                break
            if nxt:
                half = nxt
            else:
                break

        