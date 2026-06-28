class Solution:
    def countTriples(self, n: int) -> int:
        count =0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i != j:
                    s = ((i**2)+(j**2))**0.5
                    if s == int(s) and s <=n:
                        count+=1
        return count