# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        def reverse(node):
            prev = None
            while node:
                temp = node.next
                node.next = prev
                prev = node
                node = temp
            return prev
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        temp = slow
        l1= reverse(slow)
        curr = head
        while curr and curr.next != temp:
            nxt = curr.next
            curr.next = l1
            lnext = l1.next
            l1.next = nxt
            l1 = lnext
            curr = nxt
        curr.next = l1 if l1 else None
        