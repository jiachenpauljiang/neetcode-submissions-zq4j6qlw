# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_list = []
        cur_node = head

        while cur_node:
            node_list.append(cur_node)
            cur_node = cur_node.next
        
        index_to_remove = len(node_list) - n 
        if index_to_remove == 0:
            return head.next
        else:
            node_list[index_to_remove - 1].next = node_list[index_to_remove].next
        
        return head 