class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f = 0
        t = 0
        for money in bills:
            if money ==5:
                f += 1
            elif money==10:
                t+=1
                if f>=1:
                    f-=1
                else:
                    return False
            elif money == 20:
                if t>=1 and f>=1:
                    t-=1
                    f-=1
                elif f>=3:
                    f-=3
                else:
                    return False
        return True