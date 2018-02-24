class Solution:
    def singleNumber(self, nums):
        s = 0
        for i in range(len(nums)):
            s= s ^ nums[i]
        return s