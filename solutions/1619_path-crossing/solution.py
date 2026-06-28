class Solution:
    def isPathCrossing(self, path: str) -> bool:
        ini = [0,0]
        res = [(0,0)]
        for p in path:
            if(p=='N'):
                ini[0]+=1
            elif(p=='S'):
                ini[0]-=1
            elif(p=='E'):
                ini[1]+=1
            elif(p=='W'):
                ini[1]-=1
            if(tuple(ini) in res):
                return True
            res.append(tuple(ini))
        print(res)
        if(res.count(tuple(ini)) > 1):
                return True
        return False
