class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []

        for i in range(len(nums) - 1):
            j = len(nums) - 1
            while i < j:
               sum = nums[i] + nums[j]
               if sum == target:
                    arr.append(i)
                    arr.append(j)
                    j -= 1
               else:
                    j -= 1   
            
        return arr        
