class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr2 = []
        for i in range(len(arr) + k +1):
            if i not in arr:
                arr2.append(i)
        arr2.sort()        
        return arr2[k]        