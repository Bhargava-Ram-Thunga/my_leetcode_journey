class Solution:
    def findSpecialInteger(self, nums: List[int]) -> int:
        mp = dict()
        l = 0.25 * len(nums)
        for n in nums:
            if n in mp :
                mp[n] +=1
            else:
                mp[n] = 1
            if mp[n] > l:
                return n
        return -1