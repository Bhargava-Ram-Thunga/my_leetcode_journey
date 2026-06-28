class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        even = sorted(nums[::2])
        odd = sorted(nums[1::2],reverse= True)
        for i in range(n):
            if i < len(even):
                res.append(even[i])
            if i < len(odd):
                res.append(odd[i])
        return res
