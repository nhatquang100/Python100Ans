class Solution:
    def selfDividingNumbers(self, left, right):
        return [i for i in range(left,right+1) if all(int(x) != 0 and (i % int(x)) == 0 for x in str(i))]