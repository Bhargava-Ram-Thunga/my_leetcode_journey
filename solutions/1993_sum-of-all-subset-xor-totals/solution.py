class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = sum(nums)
        arr = []
        for i in range(2,len(nums)+1):
            arr.extend(list(combinations(nums,i)))
        for tup in arr:
            res += reduce(lambda x, y: x ^ y, tup)
        return res