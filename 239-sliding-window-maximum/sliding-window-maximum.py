from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()

        for index in range (0, k-1):
            while len(dq) > 0 and nums[dq[-1]] <= nums[index]: 
                dq.pop()
            dq.append(index)
        max_list = []
        
        for index in range(k-1, len(nums)):
            if index < len(nums):
                while len(dq) > 0 and nums[dq[-1]] <= nums[index]: 
                    dq.pop()
                dq.append(index)

            max_list.append(nums[dq[0]])
            if index >= dq[0] + k -1 :
                dq.popleft()
            
        return max_list