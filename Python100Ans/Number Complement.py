class Solution:
    def findComplement(self, num):
        m = 1 << (len(bin(num))-2)
        print(m)
        return (m-1) ^ num