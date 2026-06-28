class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(int(len(nums)/2)):
            Alice = min(nums)
            nums.remove(Alice)
            Bob = min(nums)
            nums.remove(Bob)
            res.append(Bob)
            res.append(Alice)
        return res