class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        [[x1,y1],[x2,y2],[x3,y3]] = points
        
        m1 = 'inf' if (x2-x1) == 0 else (y2-y1)/(x2-x1)
        m2= 'inf' if (x3-x2) == 0 else (y3-y2)/(x3-x2)
        m3 = 'inf' if (x3-x1) == 0 else (y3-y1)/(x3-x1)
        return m1 != m2 and m2!= m3 and m1!= m3