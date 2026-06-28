class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        mt =  list(zip(*matrix))
        m = list(map(set,matrix))
        mt = list(map(set,mt))
        s = set(range(1,len(matrix[0])+1))
        return mt.count(s) == m.count(s) == len(matrix)
        