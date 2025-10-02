# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseListUtil(self, head: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        temp = head.next
        head.next = prev
        if not temp:
            return head
        return self.reverseListUtil(temp, head)
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListUtil(head, None) 
            
        