class Solution:
    def reverseString(self, s):
        str = ""
        for i in s:
            str = i + str
        return str