class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        return sorted(nums,key = lambda x : (int((str(bin(x)[2:]))[::-1],2),x))