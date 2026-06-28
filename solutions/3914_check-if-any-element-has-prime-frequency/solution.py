from collections import Counter
class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        frqcy = dict(Counter(nums))
        m = max(frqcy.values())
        primes = [True] * (m+1)
        primes[0] = primes[1] = False
        p = 2
        while (p*p <= m):
            if primes[p]:
                for i in range(p*p, m+1, p):
                    primes[i] = False
            p+=1
        res = [i for i in range(len(primes)) if primes[i]==True]
        # print(res)
        # print(set(frqcy.values()))
        return any(set(frqcy.values()) & set(res))
