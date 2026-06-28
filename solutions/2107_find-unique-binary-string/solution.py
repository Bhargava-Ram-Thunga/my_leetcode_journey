class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = '1'*len(nums)
        while(n in nums):
            k = (bin(int(n,2)-1)[2:])
            n = "0"*(len(nums)-len(k))+k
        return n