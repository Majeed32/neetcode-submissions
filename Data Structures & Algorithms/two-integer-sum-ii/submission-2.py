class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            Sum = numbers[left] + numbers[right] 
            if Sum == target:
                return [left+1, right +1]
            elif Sum < target:
                left += 1
            else:
                right -= 1
        return []
        