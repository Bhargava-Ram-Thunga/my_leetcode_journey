class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        res = sorted(str(n),key = lambda x : (str(n).count(x),x))
        return int(res[0])