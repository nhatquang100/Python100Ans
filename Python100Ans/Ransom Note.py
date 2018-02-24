class Solution:
    def canConstruct(self, ransomNote, magazine):
        mag = list(magazine)
        for ch in ransomNote:
            if ch in mag:
                mag.remove(ch)
            else:
                return False
        return True