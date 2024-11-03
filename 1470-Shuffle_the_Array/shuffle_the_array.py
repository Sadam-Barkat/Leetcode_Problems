class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        subArray1 = nums[0: n]
        subArray2 = nums[n:]
        arr = []

        for i in range(len(nums) - n):
            arr.append(subArray1[i])
            arr.append(subArray2[i])
        return arr    

