class Solution:
    def isOneBitCharacter(self, bits):
        n = len(bits)
        index =0
        while index < n:
            if index == n-1 : return True
            if bits[index] == 1:
                index +=2
            else: index +=1
        return False
        