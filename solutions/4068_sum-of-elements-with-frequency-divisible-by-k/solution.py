from collections import Counter 
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = dict(Counter(nums)).items()
        res = 0
        for num,count in freq:
            if(count%k==0):
                res+=num*count
        return res