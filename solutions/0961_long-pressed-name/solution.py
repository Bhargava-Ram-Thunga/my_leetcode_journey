from itertools import groupby
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if set(name) != set(typed):
            return False
        g1 = [list(g) for k,g in groupby(name)]
        g2 = [list(g) for k,g in groupby(typed)]
        if len(g1) != len(g2):
            return False
        for i in range(len(g2)):
            c1 = g1[i][0]
            c2 = g2[i][0]
            if(c1!=c2):
                return False
            elif len(g1[i]) > len(g2[i]) :
                return False
        return True