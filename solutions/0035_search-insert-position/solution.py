class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        for num in nums:
            if num < target:
                count+=1
            else:
                break
        return count