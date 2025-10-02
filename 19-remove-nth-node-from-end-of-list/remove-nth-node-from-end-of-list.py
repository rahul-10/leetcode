# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        last = head
        count = 0
        while last and count < n:
            last = last.next
            count += 1
        
        # Assuming only valid case be there
        if not last:
            # node needs to be deleted
            return head.next
        
        temp = head
        while last and last.next:
            temp = temp.next
            last = last.next
        
        temp.next = temp.next.next 
        # node needs to be deleted

        return head
        
        

