class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_dict = Counter(nums)
        longest = 0
        for num in nums:
            count = 0
            if num -1 not in my_dict:
                count += 1
                while num + 1 in my_dict:
                    num = num + 1
                    count += 1
                longest = max(longest, count)
        return longest
        