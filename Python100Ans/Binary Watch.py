class Solution:
    def readBinaryWatch(self, num):
        output = []
        for h in range(12):
            for m in range(60):
                if bin(h* 64 +m).count('1') == num:
                    output.append('%d:%02d' %(h,m))
        return output
        