class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in nums[:]:
            nums.append(i)
        return nums    