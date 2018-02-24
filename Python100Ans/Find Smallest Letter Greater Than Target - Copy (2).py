class Solution:
    def nextGreatestLetter(self, letters, target):
        letters.sort()
        for i in letters:
            if i > target:
                return i
        return letters[0]
        