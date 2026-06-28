class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        f = {}
        for num in set(nums):
            if(num%2==0):
                f[num] = nums.count(num)
        # print(f)
        if not f:
            return -1
        res = []
        k = max(f.values())
        for n,c in f.items():
            if(c == k):
                res.append(n)
        return min(res)

