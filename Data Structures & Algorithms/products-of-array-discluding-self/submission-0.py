class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preArray = [0]*len(nums)
        sufArray = [0]*len(nums)
        preArray[0] = 1
        sufArray[-1] = 1
        for i in range(1,len(nums)):
            preArray[i] = preArray[i-1] * nums[i-1]
        prev = 1
        for i in range(len(nums)-2, -1, -1):
            sufArray[i] = sufArray[i+1] * nums[i+1]
        for i in range(len(nums)):
            sufArray[i] = sufArray[i] * preArray[i]
        return sufArray
        
