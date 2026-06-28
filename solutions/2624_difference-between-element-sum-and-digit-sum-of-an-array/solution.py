class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sumArray = sum(nums)
        sumNum = 0
        for n in nums:
            tempList = list(str(n))
            for charN in tempList:
                sumNum+=int(charN)
        return abs(sumArray-sumNum)
        