class Solution:
    def checkRecord(self, s):
        return len(s.split('A')) <=2 and s.find('LLL') == -1
        