from itertools import combinations
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        perm = list(combinations(nums,4))
        c = 0
        # print(perm)
        for li in perm:
            if sum(li[:-1]) in li:
                c += 1
        return c