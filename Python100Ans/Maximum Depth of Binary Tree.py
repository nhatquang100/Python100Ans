# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        depth = 0
        level = [root] if root else []
        while level:
            depth+=1
            queue=[]
            for i in level:
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
            level = queue
        return depth
        