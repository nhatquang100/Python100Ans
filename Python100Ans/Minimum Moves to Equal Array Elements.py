class Solution:
    def minMoves(self, nums):
        nums.sort()
        c = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == nums[0]:
                break
            c+= nums[i] - nums[0]
        return c