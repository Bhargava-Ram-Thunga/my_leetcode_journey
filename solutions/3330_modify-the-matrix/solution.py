class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        trans = list(map(list,zip(*matrix)))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = max(trans[j])
        return matrix
        