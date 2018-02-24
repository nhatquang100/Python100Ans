class Solution:
    def intersection(self, nums1, nums2):
        i=[]
        for k in nums1:
            if k in nums2 and k not in i:
                i.append(k)
        return i