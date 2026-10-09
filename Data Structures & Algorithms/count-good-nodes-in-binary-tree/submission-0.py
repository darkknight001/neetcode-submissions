# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.goodNodes = 0
        def helper(node, curmax):
            if not node:
                return


            if node.val>=curmax:
                self.goodNodes+=1
            
            curmax = max(curmax, node.val)


            helper(node.left, curmax)
            helper(node.right, curmax)

        helper(root, -101)
            
        return self.goodNodes