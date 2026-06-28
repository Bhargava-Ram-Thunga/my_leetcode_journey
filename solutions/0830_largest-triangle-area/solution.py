from itertools import combinations
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        points = map(tuple,points)
        triangles = list(combinations(points,3))
        areas = []
        for co in triangles:
            ((x1,y1),(x2,y2),(x3,y3)) = co
            a = ((x2-x1)**2 + (y2-y1)**2)**0.5
            b = ((x3-x2)**2 + (y3-y2)**2)**0.5
            c = ((x3-x1)**2 + (y3-y1)**2)**0.5
            s = (a+b+c)/2
            if(a+b>c and b+c>a and c+a>b):
                area = (s * (s-a) * (s-b) * (s-c))**0.5
                areas.append(area)
        # print(max(areas))
        return max(areas)
        