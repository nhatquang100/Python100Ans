# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        ans, L = [], [root]
        while L and root:
            ans.insert(0,[n.val for n in L])
            L = [ C for N in L  for C in (N.left, N.right) if C ]
        return ans
        