class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = list(map(list,zip(*matrix)))
        for i in range(len(matrix)):
            matrix[i][:] = (matrix[i]) [::-1]
        
        