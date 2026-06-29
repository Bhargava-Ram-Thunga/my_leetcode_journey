from collections import Counter as cs
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counts = Counter(nums)
        res = 0
        for k,v in counts.items():
            if(v==2):
                if res != 0:
                    res  ^= k
                else:
                    res = k
        return res