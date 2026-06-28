from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        di = Counter(nums)
        # for num in di:
        #     if num+1 in di:
        #         res.append(di[num]+di[num+1])
        return max([di[num]+di[num+1] if num+1 in di else 0 for num in di])
