from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        c = dict(Counter(secret))
        A = 0
        B = 0
        res = []
        for i in range(len(secret)):
            if (secret[i]==guess[i]):
                A+=1
                res.append(i)
                c[secret[i]] -= 1
        for i in range(len(secret)):
            if i not in res and guess[i] in secret and c[guess[i]] > 0 :
                B+=1
                c[guess[i]]-=1
        return f"{A}A{B}B"
            