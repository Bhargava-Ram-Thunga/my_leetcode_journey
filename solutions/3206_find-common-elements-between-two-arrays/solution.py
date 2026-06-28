class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m,n = len(nums1),len(nums2)
        ans1 = 0
        ans2 = 0
        for i in range(n):
            if nums2[i] in nums1:
                ans1+=1
        for j in range(m):
            if nums1[j] in nums2:
                ans2+=1
        return [ans2,ans1]