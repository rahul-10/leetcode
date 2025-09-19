class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = []
        current_sum = 0
        for num in nums:
            current_sum += num
            self.sum.append(current_sum)



    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right] - self.sum[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)