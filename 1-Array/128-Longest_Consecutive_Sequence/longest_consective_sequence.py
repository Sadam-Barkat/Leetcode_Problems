class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        res = 1
        l = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                l += 1
            else:
                l = 1
            res = max(res, l)

        return res