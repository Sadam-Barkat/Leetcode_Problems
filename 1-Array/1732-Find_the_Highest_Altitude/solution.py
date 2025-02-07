class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        arr = [0]
        a = 0

        for i in gain:
            a = i + a
            arr.append(a)

        return max(arr)    
             
