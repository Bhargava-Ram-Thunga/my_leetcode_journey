class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        rays = []
        for lasers in bank:
            if lasers.count("1") != 0:
                rays.append(lasers.count("1"))
        res = 0
        for i in range(1,len(rays)):
            res += rays[i]*rays[i-1]
        return res