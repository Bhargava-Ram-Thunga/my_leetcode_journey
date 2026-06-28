class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        dif = []
        res = []
        for i in range(1,int((area)**0.5)+1):
            l = area/i
            w = i
            if w > l:
                l,w = w,l
            if((l).is_integer()):
                dif.append(abs((area/i) - i))
                res.append([int(l),w])
        mini = dif.index(min(dif))
        return res[mini]