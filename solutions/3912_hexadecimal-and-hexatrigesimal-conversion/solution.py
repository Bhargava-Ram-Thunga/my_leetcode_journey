class Solution:
    def concatHex36(self, n: int) -> str:
        k = n**3
        arrAlp = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        res = []
        while(k>=36):
            res.append((k%36))
            k//=36
        arrAns = "".join([ arrAlp[res[i]] for i in range(len(res))][::-1])
        ans = arrAlp[k]+arrAns
        return (hex(n**2)[2:]).upper() + ans