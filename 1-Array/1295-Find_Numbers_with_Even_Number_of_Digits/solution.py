class Solution:
    def findNumbers(self, nums: List[int]) -> int:
       count = 0
       for i in nums:
        List = list(str(i))
        if len(List) %  2 == 0:
            count += 1
       return count    


