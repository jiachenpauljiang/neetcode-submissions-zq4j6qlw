# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half_head = slow.next
        slow.next = None 

        # reversing the second half 
        prev = None
        while second_half_head:
            temp_next = second_half_head.next
            second_half_head.next = prev
            prev = second_half_head
            second_half_head = temp_next
        # now prev is the head of the reversed second part of the list 

        first, second_half_head = head, prev
        while second_half_head:
            temp1, temp2 = first.next, second_half_head.next
            first.next = second_half_head
            second_half_head.next = temp1
            first, second_half_head = temp1, temp2
