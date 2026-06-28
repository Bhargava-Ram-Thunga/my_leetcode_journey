class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        temp = []
        for li in mat:
            temp.extend(li)
        res = []
        for i in range(0,len(temp),c):
            res.append(temp[i:i+c])
        return res