class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        arr = []
        for i in range(len(s2) - len(s1) + 1):
            if(sorted(s2[i : i + len(s1)]) == s1):
                arr.append(i)
        if not arr:
            return False
        else:
            return True          

