# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        dummy = ListNode(-1, head)
        temp = dummy
        curr = head
        while curr:
            length += 1
            curr = curr.next
        while length >= k:
            nxt_end = temp.next
            for _ in range(k-1):
                node = nxt_end.next
                nxt_end.next = nxt_end.next.next
                node.next = temp.next
                temp.next = node
            temp = nxt_end
            length -= k
        return dummy.next



        