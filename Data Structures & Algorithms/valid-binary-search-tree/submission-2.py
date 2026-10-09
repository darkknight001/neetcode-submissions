# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lb, ub):
            if not node:
                return True
            
            left = helper(node.left, lb, node.val)
            current = node.val>lb and node.val<ub
            right = helper(node.right, node.val, ub)
            return current and left and right

        return helper(root, float("-inf"), float('inf'))