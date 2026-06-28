class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return []
        i = 0
        res= []
        while i<m*n:
            res.append(original[i:i+n])
            i+=n
        return res