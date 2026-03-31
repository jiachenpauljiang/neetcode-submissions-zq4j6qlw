# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, curDepth):
            if not node:
                return curDepth
            return (1 + max(dfs(node.left, curDepth), dfs(node.right, curDepth)))
        
        return dfs(root, 0)

            