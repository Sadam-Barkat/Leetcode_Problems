class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1 = sorted(arr1)
        extra_elements = []  
        sorted_elements = []  
        
        element_count = {}  
        
        for num in arr1:
            if num in arr2:
                if num in element_count:
                    element_count[num] += 1
                else:
                    element_count[num] = 1
            else:
                extra_elements.append(num)  
        
        for num in arr2:
            count = element_count[num]
            for _ in range(count):
                sorted_elements.append(num)
        
        sorted_elements.extend(extra_elements)
        
        return sorted_elements
