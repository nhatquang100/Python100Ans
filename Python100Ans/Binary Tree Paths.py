# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        res, queue = [], collections.deque([(root,"")])
        while queue:
            node, ls = queue.popleft()
            if not node.left and not node.right:
                res.append(ls + str(node.val))
            if node.right:
                queue.append((node.right, ls+str(node.val)+"->"))
            if node.left:
                queue.append((node.left, ls+str(node.val)+"->"))
        return res