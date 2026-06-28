class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        res = []
        for i in range(len(coordinates)):
            if i == len(coordinates) -1:
                x1,y1 = coordinates[i]
                x2,y2 = coordinates[0]
            else:
                x1,y1 = coordinates[i]
                x2,y2 = coordinates[i+1]
            if (x2-x1) == 0:
                res.append('inf')
            else:
                res.append((y2-y1)/(x2-x1))
        res = set(res)
        return len(res) == 1
