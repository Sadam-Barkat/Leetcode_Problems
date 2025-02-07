class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d={}
        for index,ele in enumerate(nums):
            d[ele]=index
        for old,new in operations:
            nums[d[old]] = new
            d[new]=d[old]
        return nums