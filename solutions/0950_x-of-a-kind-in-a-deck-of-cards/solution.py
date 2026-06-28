class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if(len(deck)==1):
            return False
        if len(deck) == 2:
            return True
        return reduce(math.gcd,dict(Counter(deck)).values()) != 1