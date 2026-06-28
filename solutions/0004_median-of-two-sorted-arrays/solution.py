class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1+nums2)
        l = len(nums)
        if l%2:
            return float(nums[(l-1)//2])
        else:
            return sum(nums[(l-2)//2:((l-2)//2)+2])/2