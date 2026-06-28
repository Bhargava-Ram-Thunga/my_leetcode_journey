class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j or i+j == len(mat[i])-1:
                    res += mat[i][j]
        return res