import itertools
import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result_node = temp = ListNode()
        
        counter = itertools.count()

        heap = [(head.val, next(counter), head) for head in lists if head]

        heapq.heapify(heap)
        
        while heap:
            _, _, node = heapq.heappop(heap)
            temp.next = node
            temp = temp.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, next(counter), node.next))

        return result_node.next

            
        