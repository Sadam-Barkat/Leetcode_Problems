class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        stack = []
        nums.sort()

        for val in nums:
            if stack and stack[-1] == val:
                stack.pop()
            else:
                stack.append(val)    
        return stack[-1]       
        

         