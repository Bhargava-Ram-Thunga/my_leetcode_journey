class Solution:
    def containsPattern(self, nums: List[int], m: int, k: int) -> bool:
        pr = []
        for i in range(len(nums)-m):
            pr.append(tuple(nums[i:i+m]))
        pr = set(pr)
        pr = list(map(list,pr))
        for pattern in pr :
            # print(str(pattern*k)[1:-1])
            if (str(pattern*k)[1:-1]) in str(nums):
                return True
        return False
