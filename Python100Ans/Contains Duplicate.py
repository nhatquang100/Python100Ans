class Solution:
    def containsDuplicate(self, nums):
        c = collections.Counter(nums)
        for i in c.values():
            if i != 1 :
                return True
        return False