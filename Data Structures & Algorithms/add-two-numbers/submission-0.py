# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy
        carry = 0
        while l1 or l2 or carry:
            Sum = 0
            if l1:
                Sum += l1.val
                l1 = l1.next
            if l2:
                Sum += l2.val
                l2 = l2.next
            carry, nodeValue = divmod(Sum + carry, 10)
            newNode = ListNode(nodeValue)
            temp.next = newNode
            temp = temp.next
        return dummy.next
    