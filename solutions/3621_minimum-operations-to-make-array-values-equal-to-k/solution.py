class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        temp = min(nums)
        temp2 = len(set(nums))
        if temp < k :
            return -1
        if temp == k:
            return temp2-1
        return temp2