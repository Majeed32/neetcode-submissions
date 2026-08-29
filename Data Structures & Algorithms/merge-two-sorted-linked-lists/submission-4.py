# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode(-1)
        temp = new
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    next = list1.next
                    list1.next = None
                    temp.next = list1
                    temp = temp.next
                    list1 = next
                else:
                    next = list2.next
                    list2.next = None
                    temp.next = list2
                    temp = temp.next
                    list2 = next
            elif list1:
                temp.next = list1
                break
            else:
                temp.next = list2
                break
        return new.next

        