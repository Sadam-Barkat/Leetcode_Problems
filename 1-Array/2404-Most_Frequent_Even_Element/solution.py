class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dict1 = {}
        arr = []
        for i in nums:
            if i % 2 == 0:
                if i in dict1:
                    dict1[i] += 1
                else:
                    dict1[i] = 1
        if not dict1:
            return -1            
        for key, val in dict1.items():
            if val == max(dict1.values()):
                arr.append(key) 
        return min(arr)    

        