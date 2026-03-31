# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        stack = [root]

        while stack:
            curRoot = stack.pop()

            curRoot.left, curRoot.right = curRoot.right, curRoot.left

            if curRoot.left:
                 stack.append(curRoot.left)
            if curRoot.right:
                stack.append(curRoot.right)
        return root