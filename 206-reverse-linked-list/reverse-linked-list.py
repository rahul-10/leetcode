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
        # return self.reverseListUtil(head, None) 
        if not head or not head.next:
            return head
        
        temp = head.next
        curr = head

        while temp:
            curr.next = temp.next
            temp.next = head
            head = temp
            temp = curr.next
        return head
            
        