class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_candies = sum(aliceSizes)
        bobSet = set(bobSizes)
        q = (alice_candies+(sum(bobSizes)))//2
        for c in set(aliceSizes):
            t = q-(alice_candies-c)
            if t in bobSet:
                return([c,t])
        return [-1,-1]