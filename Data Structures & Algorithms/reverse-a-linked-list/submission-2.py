# Definition for singly-linked list.
# class ListNode:
from os import preadv
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        
        def reverse(cur, prev):
            if cur is None:
                return prev 
            else:
                next = cur.next
                cur.next = prev 
            return reverse(next, cur)
        
        return reverse(head, None)



