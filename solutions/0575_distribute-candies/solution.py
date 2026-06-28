class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        temp = set(candyType)
        return min(int(len(candyType)/2),int(len(temp)))