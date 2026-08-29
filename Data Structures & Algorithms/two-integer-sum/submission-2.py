class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, n in enumerate(nums):
            rem = target-n
            if rem in seen:
                return [seen[rem], idx]
            seen[n] = idx
        return [-1, -1]
        