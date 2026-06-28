class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ind = []
        for i,row in enumerate(matrix):
            for j,val in enumerate(row):
                if val == 0:
                    ind.append([i,j])
        temp = matrix
        for i,j in ind:
            temp[i] = [0]*len(temp[i])
        temp = list(map(list,zip(*temp)))
        for i,j in ind :
            temp[j] = [0] * len(temp[j])
        temp = list(map(list,zip(*temp)))
        matrix[:] = temp
        # return matrix
        