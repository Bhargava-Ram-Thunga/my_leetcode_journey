class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = 0
        c = 0
        for i in s:
            if i in "aeiou":
                v+=1
            elif i in "bcdfghjklmnpqrstvwxyz":
                c+=1
        return v//c if c !=0 else 0