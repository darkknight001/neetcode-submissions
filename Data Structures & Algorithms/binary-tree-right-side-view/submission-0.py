# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        arr = []
        q = deque()
        q.append((root, 1))
        while(q):
            node, level = q.popleft()
            if node:
                if len(arr)<level:
                    if arr:
                        ans.append(arr[-1][-1])
                    arr.append([])
                arr[-1].append(node.val)
                q.append((node.left, level+1))
                q.append((node.right, level+1))
        if arr:
            ans.append(arr[-1][-1])
        return ans