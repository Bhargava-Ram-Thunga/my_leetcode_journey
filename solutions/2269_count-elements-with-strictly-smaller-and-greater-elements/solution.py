class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        temp = sorted(set(nums))
        res = 0
        for i in range(1,len(temp)-1):
            res += count[temp[i]]
        return res