class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        left = 0
        for i in range(len(nums) - 1):
            right = len(nums) - 1
            while left < right:
                if nums[left] == nums[right]:
                    count += 1
                    right -= 1
                else:
                    right -= 1
            left += 1
        return count         
