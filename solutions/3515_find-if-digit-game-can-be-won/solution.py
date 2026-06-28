class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = []
        double = []
        for num in nums:
            if num < 10:
                single.append(num)
            else:
                double.append(num)
        return sum(single) != sum(double)