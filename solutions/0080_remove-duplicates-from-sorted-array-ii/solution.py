class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dictCount = Counter(nums)
        nums[:] = []
        for num,count in dictCount.items():
            if count > 2:
                nums.extend([num]*2)
            else:
                nums.extend([num]*count)
        return len(nums)
        
            