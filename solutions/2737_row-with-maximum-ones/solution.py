class Solution:
    def rowAndMaximumOnes(self, matrix: List[List[int]]) -> List[int]:
        temp = []
        for i in range(len(matrix)):
            temp.append(matrix[i].count(1))
        res = []
        maxi = max(temp)
        ind = temp.index(maxi)
        return [ind,maxi]

