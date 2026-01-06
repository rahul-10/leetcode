class Solution:
    def append_in_maxima(self, maxima: list[int], height: list[int], index: int) -> None:
        while len(maxima) >= 2 and height[maxima[-2]] >= height[maxima[-1]] <= height[index] :
            maxima.pop()
        maxima.append(index)

    def trap(self, height: List[int]) -> int:
        if len(height) <=2:
            return 0

        maxima = []
        if height[0] >= height[1]:
            maxima.append(0)
        
        for i in range(1, len(height)-1):
            if height[i-1] <= height[i] >= height[i+1]:
                self.append_in_maxima(maxima, height, i)
                continue
        
        if height[-1] >= height[-2]:
            self.append_in_maxima(maxima, height, len(height)-1)
        
        print('maxima: ', maxima)
        total=0
        for i in range(1, len(maxima)):
            left , right = maxima[i-1], maxima[i]
            min_val = min(height[left], height[right])
            for j in range(left+1, right):
                total += max(min_val - height[j], 0)
        
        return total
            

        

        