class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)[::-1]
        if n<1000:
            return s[::-1]
        temp = []
        k = 0
        while k < len(s):
            temp.append((s[k:k+3])[::-1])
            k+=3
        return ".".join(temp[::-1])
