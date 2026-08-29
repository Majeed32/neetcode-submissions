# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val : idx for idx, val in enumerate(inorder)}
        def build(inorder_start, inorder_end, preorder_start, preorder_end):
            if preorder_end < preorder_start:
                return
            val = preorder[preorder_start]
            root = TreeNode(val)
            idx = inorder_map[val]
            left = idx - inorder_start
            root.left = build(inorder_start, idx-1, preorder_start + 1, preorder_start + left)
            root.right = build(idx + 1, inorder_end, preorder_start + left + 1, preorder_end)
            return root
        return build(0, len(inorder)-1, 0, len(preorder)-1)
        