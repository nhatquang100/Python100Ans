class Solution:
    def nextGreaterElement(self, nums1, nums2):
        cache, st = {}, []
        for x in nums2:
            while st and st[-1] < x:
                cache[st.pop()] = x
            st.append(x)
        result = [-1]* len(nums1)
        for idx,x in enumerate(nums1):
            if x in cache:
                result[idx] = cache[x]
        return result
        