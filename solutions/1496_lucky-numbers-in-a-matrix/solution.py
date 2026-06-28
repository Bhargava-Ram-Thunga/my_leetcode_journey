class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[List[int]]:
        mat_trans = list(map(list,zip(*matrix)))
        mins = set()
        maxs = set()
        for li in matrix:
            mins.add(min(li))
        for li in mat_trans:
            maxs.add(max(li))
        return list(mins & maxs)