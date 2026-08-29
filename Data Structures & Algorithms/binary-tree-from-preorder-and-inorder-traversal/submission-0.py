# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        myMap = {val:idx for idx, val in enumerate(inorder)}
        def construct(ileft, iright, pleft, pright):
            if pleft > pright:
                return
            root = TreeNode(preorder[pleft])
            idx = myMap[root.val]
            left_size = idx - ileft
            root.left = construct(ileft, idx-1, pleft+1, pleft + left_size)
            root.right = construct(idx + 1, iright, pleft + left_size + 1, pright)
            return root
        return construct(0, len(inorder)- 1, 0, len(preorder)-1)
        