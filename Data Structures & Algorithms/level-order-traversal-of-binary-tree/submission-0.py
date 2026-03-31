# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        # the result list holding all the level specific lists
        res = [] 

        # the queue holding nodes in processing 
        cur_nodes_queue = deque()
        cur_nodes_queue.append(root)

        while cur_nodes_queue:
            cur_level_num_of_nodes = len(cur_nodes_queue)
            cur_level_list = []

            for node in range(cur_level_num_of_nodes):
                cur_node = cur_nodes_queue.popleft()
                if cur_node:
                    cur_level_list.append(cur_node.val)
                    cur_nodes_queue.append(cur_node.left)
                    cur_nodes_queue.append(cur_node.right)
            if cur_level_list:
                res.append(cur_level_list)
        
        return res
