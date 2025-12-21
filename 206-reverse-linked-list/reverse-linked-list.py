# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        prev = head
        curr = prev.next

        while curr: 
            prev.next = curr.next
            curr.next = head
            head = curr
            curr = prev.next

        return head
        