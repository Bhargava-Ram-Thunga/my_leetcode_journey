class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c = []
        for i in range(len(A)):
            c.append(len(set(A[:i+1])& set(B[:i+1])))
        return c