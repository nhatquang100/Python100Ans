class Solution:
    def findTarget(self, root, k):
        a = set()
        self.f = False
        def dfs(root, k):
            if not root:
                return
            if root.val not in a:
                a.add(k- root.val)
            else:
                self.f = True
            dfs(root.left, k)
            dfs(root.right, k)
        dfs(root, k)
        return self.f
        