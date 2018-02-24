class Solution:
    def findTheDifference(self, s, t):
         return list(collections.Counter(t) - collections.Counter(s))[0]
        