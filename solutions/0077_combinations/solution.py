from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        c = list(map(list,list(combinations(list(range(1,n+1)),k))))
        # print(c)
        return c