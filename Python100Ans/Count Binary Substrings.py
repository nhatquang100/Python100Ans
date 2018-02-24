class Solution:
    def countBinarySubstrings(self, s):
        arr, consecutive, res = [], 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                consecutive +=1
            else:
                arr.append(consecutive)
                consecutive = 1
        arr.append(consecutive)
        for i in range(1, len(arr)):
            res += min(arr[i], arr[i-1])
        return res 