from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)


        freq = Counter(nums)
        freq = {key: 1 for key in freq}
        # print('freq: ', freq)
        visited = {}

        max_count = 0
        for num in nums:
            # print('===> num: ', num)    
            current_count = freq[num]
            currect_num = num
            while not visited.get(num, False):
                visited[num] = True
                num = num+1
                # print('loop num: ', num)    
                current_count = current_count + freq.get(num, 0)
                # print('loop current_count: ', current_count, ', max_count: ', max_count)    
                if max_count < current_count:
                    max_count = current_count
                # print('loop freq.get(num, 0): ', freq.get(num, 0), ', visited.get(num , True): ', visited.get(num , True))    
                if not freq.get(num) or visited.get(num , False):
                    freq[currect_num] = current_count
                    break 
            # print('freq: ', freq) 
            # print('visited: ', visited)
            # print('max_count: ', max_count)              
                
        return max_count
            