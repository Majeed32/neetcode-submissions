class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        my_dict = Counter(nums)
        my_nums = [(-my_dict[num], num) for num in my_dict]
        heapq.heapify(my_nums)
        for i in range(k):
            res.append(heapq.heappop(my_nums)[1])
        return res

        