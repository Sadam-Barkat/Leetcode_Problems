class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = []
        runingSum = 0

        for i in range(len(nums)):
            runingSum = nums[i] + runingSum
            arr.append(runingSum)
        return arr    
