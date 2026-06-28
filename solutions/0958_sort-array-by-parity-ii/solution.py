class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        res = []
        for num in nums:
            if num%2:
                odd.append(num)
            else:
                even.append(num)
        for i in range(len(nums)//2):
            res.append(even[i])
            res.append(odd[i])
        return res