class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    pass
                elif arr[i] == arr[j] / 2:
                    return True         
        return False
    