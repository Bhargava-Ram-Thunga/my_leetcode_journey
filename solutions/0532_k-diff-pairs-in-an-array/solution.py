class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ns = set(nums)
        f = dict(Counter(nums))
        res = 0
        print(f.values())
        if k == 0:
            return len([i for i in f.values() if i > 1])
        for num in ns:
            if num - k in ns:
                res+= 1
        return res