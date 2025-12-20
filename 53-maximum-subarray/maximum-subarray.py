import sys


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        largest_sum = current_sum = nums[0]

        for inx, val in enumerate(nums[1:], start=1):
            if current_sum < 0:
                current_sum = 0
            current_sum = current_sum + val

            if current_sum > largest_sum:
                largest_sum = current_sum

        return largest_sum
