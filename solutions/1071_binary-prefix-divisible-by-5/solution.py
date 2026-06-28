class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        nums = list(map(str,nums))
        return [True if (int("".join(nums[:i+1]),2)%5==0) else False for i in range(len(nums))]