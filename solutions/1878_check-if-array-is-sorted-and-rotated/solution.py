class Solution:
    def check(self, nums: List[int]) -> bool:
        li = sorted(nums)
        for i in range(len(nums)+1):
            if li==nums:
                return True
            else:
                nums.insert(0,nums.pop())
        return False