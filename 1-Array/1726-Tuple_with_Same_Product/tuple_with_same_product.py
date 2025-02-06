class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        product_count = {} 
        n = len(nums)
        result = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                if product in product_count:
                    product_count[product] += 1
                else:
                    product_count[product] = 1
        
 
        for count in product_count.values():
            if count > 1:
                result += (count * (count - 1) // 2) * 8 

        return result
