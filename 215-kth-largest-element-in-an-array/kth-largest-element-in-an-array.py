import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = [nums[i] for i in range(0, k)]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
        return heap[0]
        