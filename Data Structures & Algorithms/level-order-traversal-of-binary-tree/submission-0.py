# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = []
        if not root:
            return []
        q.append((root, 0))
        cl = []
        ll = 0
        while(q):
            node, level = q.pop(0)
            if level == ll:
                cl.append(node.val)
            else:
                ll=level
                ans.append(cl)
                cl = [node.val]
            
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        if cl:
            ans.append(cl)
        return ans