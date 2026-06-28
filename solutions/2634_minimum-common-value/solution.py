class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        x = set(nums1) & set(nums2)
        if(x):
            return min(x)
        return -1