# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy
        heap = []
        for idx, head in enumerate(lists):
            if not head:
                continue
            heap.append((head.val, idx))
        heapq.heapify(heap)
        while heap:
            val, idx = heapq.heappop(heap)
            temp.next = lists[idx]
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
            temp = temp.next
        return dummy.next
            
        