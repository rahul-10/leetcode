import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:        
        nums = []
        counter = count()

        for head in lists:
            if head:
                heapq.heappush(nums, (head.val, next(counter),  head))

        dummy_head = ListNode(0)
        curr = dummy_head

        while len(nums):
            _, _, node = heappop(nums)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(nums, (node.next.val, next(counter), node.next))
            
        return dummy_head.next