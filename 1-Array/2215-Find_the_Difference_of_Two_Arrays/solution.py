class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        arr1 = []
        arr2 = []
        arr3 = []

        for i in nums1:
            if i not in nums2:
                arr1.append(i)
        arr3.append(arr1)

        for j in nums2:
            if j not in nums1:
                arr2.append(j)
        arr3.append(arr2)  

        return arr3      
        