class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        someDict = {}
        for i in range(len(nums1)):
            someDict[nums1[i][0]] = nums1[i][1]
        for i in range(len(nums2)):
            if nums2[i][0] in someDict:
                someDict[nums2[i][0]] += nums2[i][1]
            else:
                someDict[nums2[i][0]] = nums2[i][1]
        return list(map(list,sorted(someDict.items())))