class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersection = set()
        i , j = 0 , 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersection.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1 
            else:
                i += 1
        arr = []
        for i in intersection:
            arr.append(i)
        return arr    