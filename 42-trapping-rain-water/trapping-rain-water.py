class Solution:

    def find_sum(self, height, left, right):
        min_height = min(height[left], height[right])
        total_sum = 0
        for index in range(left+1, right):
            total_sum += 0 if (min_height - height[index]) <=0 else (min_height - height[index])
        
        return total_sum

    def update_local_maxima(self, height, local_maxima, index):
        if len(local_maxima) >= 2 and height[index] >= height[local_maxima[-1]]:
            while len(local_maxima) >1 and height[index] >= height[local_maxima[-1]] and height[local_maxima[-2]] >= height[local_maxima[-1]]:
                local_maxima.pop()
            local_maxima.append(index)      
        else:
            local_maxima.append(index)

    def find_local_maxima(self, height):
        local_maxima = []
        local_maxima.append(0)

        for index in range(1, len(height)-1):
            if height[index] >= height[index-1] and height[index] >= height[index+1]:
                self.update_local_maxima(height, local_maxima, index)

        if height[len(height)-1] >= height[len(height)-2]:
            self.update_local_maxima(height, local_maxima, len(height)-1)
        return local_maxima

    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <=2: 
            return 0
        
        local_maxima = self.find_local_maxima(height)
        print('local_maxima: ', local_maxima)
        if len(local_maxima) < 2:
            return 0
        
        total_water = 0
       
        left_index = local_maxima[0]
        for index in range(1, len(local_maxima)):
            right_index = local_maxima[index]
            total_water += self.find_sum(height, left_index, right_index)
            left_index = right_index

        return total_water

        
        
