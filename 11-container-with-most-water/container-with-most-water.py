class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0
        while(left < right):
            max_area = max(max_area, min(height[left], height[right]) * (right-left))
            if height[left] < height[right]:
                left += 1
                continue
            right -= 1
        
        return max_area
            
            
        




















        # left = 0 
#         right = len(height)-1
#         max_area = 0
#         while left<right:
#             # print(f'left: {left}, right: {right}, output: {(right-left) * min(height[left], height[right])}' )
#             x = (right-left) * min(height[left], height[right])
#             if x > max_area:
#                 max_area = (right-left) * min(height[left], height[right])

#             if height[left] < height[right]:
#                 left += 1
#             else:
#                 right -= 1
#         return max_area

        