# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        count = 1
        while curr.next:
            curr = curr.next
            count += 1
        dummy = ListNode(-1, head)
        i = 1
        res = dummy
        curr = head
        while count >= k:
            for _ in range(k-1):
                temp = curr.next
                curr.next = curr.next.next
                temp.next = res.next
                res.next = temp
            count -= k
            res = curr
            curr = curr.next
        return dummy.next



        