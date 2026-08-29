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
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow.next
        slow.next = None
        new_head = reverse(temp)
        
        curr = head
        while new_head:
            tmp, nxt= curr.next, new_head.next
            curr.next = new_head
            new_head.next = tmp
            curr, new_head = tmp, nxt