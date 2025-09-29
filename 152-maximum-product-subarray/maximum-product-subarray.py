class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product  = nums[0]
        current_prod = 1
        for i in range(0, len(nums)):
            current_prod = current_prod * nums[i]
            if max_product < current_prod:
                max_product = current_prod
            if current_prod == 0:
                current_prod = 1
        
        current_prod = 1

        for i in range(len(nums)-1, -1, -1):
            current_prod = current_prod * nums[i]
            if max_product < current_prod:
                max_product = current_prod
            if current_prod == 0:
                current_prod = 1

        return max_product