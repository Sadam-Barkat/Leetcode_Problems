class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_num = nums[len(nums) - 1]
        for i in range(1, k):
            max_num = max_num + nums[len(nums) - 1] + i
        return max_num    