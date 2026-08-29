# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root, p, q):
            if not root:
                return
            if root.val < p.val and root.val < q.val:
                return dfs(root.right, p, q)
            if root.val > p.val and root.val > q.val:
                return dfs(root.left, p, q)
            return root
        return dfs(root, p, q)