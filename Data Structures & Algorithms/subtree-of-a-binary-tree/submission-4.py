# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node2:
                return True
            if not node1:
                return False
            if same(node1, node2):
                return True
            return dfs(node1.left, node2) or dfs(node1.right, node2)
        
        def same(node1, node2):
            if not node1 and not node2:
                    return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and same(node1.left, node2.left) and same(node1.right, node2.right)
        return dfs(root, subRoot)

        