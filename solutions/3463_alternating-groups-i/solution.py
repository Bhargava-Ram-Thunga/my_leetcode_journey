class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        r = 0
        c = len(colors)
        colors += colors
        for i in range(c):
            comp = colors[i:i+3]
            if(comp[0]==comp[-1] and comp[0]!=comp[1]):
                r+=1
        return r