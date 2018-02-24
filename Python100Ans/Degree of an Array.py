class Solution:
    def findShortestSubArray(self, nums):
        if nums == []:
            return 0
        degree = max(collections.Counter(nums).values())
        so_far = collections.defaultdict(int)
        min_size = len(nums)
        start, end = 0, len(nums)-1
        for end, num in enumerate(nums):
            so_far[num] += 1
            while start <= end and so_far[num] == degree:
                min_size = min(min_size, end-start+1)
                so_far[nums[start]] -= 1
                start += 1
        return min_size