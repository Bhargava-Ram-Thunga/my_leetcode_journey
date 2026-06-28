class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        summ = 0
        for num in str(n):
            prod*=int(num)
            summ+=int(num)
        return prod-summ