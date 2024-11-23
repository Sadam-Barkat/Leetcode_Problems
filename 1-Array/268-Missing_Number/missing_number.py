class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        List = list(range(len(nums)+1))
        for val in List:
            if val not in nums:
                return val
