class Solution:
    def isPowerOfFour(self, num):
        s= 1
        while s < num:
            s*=4
        if s == num:
            return True
        return False