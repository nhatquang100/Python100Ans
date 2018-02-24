class Solution:
    def tree2str(self, t):
        s =''
        if not t:
            return ''
        s+=str(t.val)
        if t.left or t.right:
            s+='('+self.tree2str(t.left)+')'
        if t.right:
            s+='('+self.tree2str(t.right)+')'
        return s
        