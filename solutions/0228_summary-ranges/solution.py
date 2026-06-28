class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if(not nums):
            return []
        s = nums[0]
        e = nums[0]
        res = []
        for i in range(len(nums)-1):
            if(nums[i]+1==nums[i+1]):
                e = nums[i+1]
            else:
                if(s==e):
                    res.append(f"{s}")
                else:
                    res.append(f"{s}->{e}")
                s = nums[i+1]
                e = nums[i+1]
        if(s!=e):
            res.append(f"{s}->{e}")
        else:
            res.append(f"{nums[-1]}")
        return res
