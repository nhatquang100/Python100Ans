# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        def helper(root,level):
            if not root:
                return
            self.ans[level] += [root.val]
            helper(root.left, level+1)
            helper(root.right, level+1)
            
        if not root:
            return []
        self.ans = collections.defaultdict(list)
        result = []
        helper(root, 1)
        for key, value in self.ans.items():
            result.append(float(sum(value))/len(value))
        return result