class Solution:
    def distributeCandies(self, candies):
        tmp = len(candies)//2
        s = set(candies)
        if len(s) < tmp:
            return len(s)
        return tmp