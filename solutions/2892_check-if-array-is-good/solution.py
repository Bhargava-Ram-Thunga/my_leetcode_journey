class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)
        c = dict(Counter(nums))
        l = set()
        # print(c)
        for k,v in c.items():
            if v > 1:
                l.add(k)
            print(l)
            if(len(l) > 1):
                return False
        print(len(l) , 1)
        print(len(c.keys()), m)

        return len(l) == 1 and len(c.keys()) == m and nums.count(m) == 2