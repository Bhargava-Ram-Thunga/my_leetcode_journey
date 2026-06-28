from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        m = list(dict(filter(lambda x : x[1]==1,m.items())).keys())
        return m

