class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            strnum = str(i)
            lenstr = len(strnum)
            if lenstr%2 ==0:
                lnum = list(map(int,list(strnum[:lenstr//2])))
                rnum = list(map(int,list(strnum[lenstr//2:])))
                if sum(lnum)==sum(rnum):
                    count += 1
        return count


