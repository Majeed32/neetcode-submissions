# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        heap = []
        for idx, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, idx))
        while heap:
            val, idx = heapq.heappop(heap)
            node = lists[idx]
            temp.next = node
            lists[idx] = node.next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
            temp = temp.next
        return dummy.next

        