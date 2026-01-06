class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        max_value = nums[0]
        max_index = 0
        n = len(nums)
        for i in range(1, n):
            if max_value < nums[i]:
                max_value = nums[i]
                max_index = i
        
        result = [-1] * n
        stack = [nums[max_index]]
        i = (max_index - 1) + n

        while i % n != max_index:
            while stack and  stack[-1] <= nums[i % n]:
                stack.pop()
            if stack:
                result[i % n] = stack[-1]
            stack.append(nums[i % n])
            
            i = i-1

        return result
        