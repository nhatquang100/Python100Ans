class Solution:
    def longestPalindrome(self, s):
        a = collections.Counter(s)
        ret = 0
        singlechar =0
        for i in a.values():
            if i % 2 == 0:
                ret += i
            else:
                ret += i -1
                singlechar = 1
        return ret + singlechar