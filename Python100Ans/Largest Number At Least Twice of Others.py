class Solution:
    def dominantIndex(self, nums):
        return nums.index(max(nums)) if all(max(nums) >= num * 2 for num in nums if num             != max(nums)) else -1
        
        