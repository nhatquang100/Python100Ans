class Solution:
    def isAnagram(self, s, t):
        if sorted(s) == sorted(t):
            return True
        return False