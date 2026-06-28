class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0
        nums = list(map(str,nums))
        for i in nums:
            if len(i) == 1:
                res += int(i)
            else:
                temp = list(map(int,i))
                maxi = max(temp)
                num = int(str(maxi)*len(temp))
                res += num
        return res