class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if(set(nums1)&set(nums2)):
            return min(set(nums1)&set(nums2))
        return min(int(str(min(nums1))+str(min(nums2))),int(str(min(nums2))+str(min(nums1))))