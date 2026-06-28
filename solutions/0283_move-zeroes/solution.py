class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums[:] = sorted(nums , key = lambda x : x==0 )
        