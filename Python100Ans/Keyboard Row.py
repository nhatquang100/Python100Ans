class Solution:
    def findWords(self, words):
        a = set("qwertyuiop")
        b = set("asdfghjkl")
        c = set("zxcvbnm")
        ans=[]
        for i in words:
            t = set(i.lower())
            if a&t == t:
                ans.append(i)
            if b&t == t:
                ans.append(i)
            if c&t == t:
                ans.append(i)
        return ans