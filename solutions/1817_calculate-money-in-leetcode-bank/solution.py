class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        count = 1
        while (n > 0):
            if n > 7:
                res += sum(list(range(count,count+7)))
                count += 1
                n-=7
            else:
                res = res + sum(list(range(count,count+n)))
                n-=n
        return res