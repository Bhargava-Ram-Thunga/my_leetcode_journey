class Solution:
    def averageValue(self, nums: List[int]) -> int:
        c = 0
        res = 0
        for num in nums:
            if not(num%6):
                c+=1
                res+=num
        if c==0:
            return 0
        return int(res/c)