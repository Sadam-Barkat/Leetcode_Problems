class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0

        product = 1
        left = 0
        res = 0

        for right in range(len(nums)):
            product *= nums[right]  

            while product >= k and left <= right:
                product = product // nums[left]
                left += 1
            res = res + right - left + 1
        return res         