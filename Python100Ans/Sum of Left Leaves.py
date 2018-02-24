# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        sum = self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        if root.left and not root.left.left and not root.left.right:
            sum += root.left.val
        return sum