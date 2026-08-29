# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("N")
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) < 1 or data == "N":
            return
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        idx = 1
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if nodes[idx] != "N":
                node.left = TreeNode(int(nodes[idx]))
                queue.append(node.left)
            idx += 1
            if idx < len(nodes) and nodes[idx] != "N":
                node.right = TreeNode(int(nodes[idx]))
                queue.append(node.right)
            idx += 1
        return root
