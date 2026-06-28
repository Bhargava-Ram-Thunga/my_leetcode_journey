class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            if (nums1[i] in nums2 or nums1[i] in nums3) and nums1[i] not in res:
                res.append(nums1[i])
        for i in range(len(nums2)):
            if (nums2[i] in nums3 or nums2[i] in nums1 )and nums2[i] not in res:
                res.append(nums2[i])
        return res