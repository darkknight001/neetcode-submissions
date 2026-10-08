# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 0
            
            lh = helper(node.left)
            rh = helper(node.right)
            if lh ==-1 or rh ==-1 or abs(lh-rh)>1:
                return -1
            return max(lh, rh)+1
        
        if not root:
            return True
        return helper(root)!=-1