class Solution:
    def secondHighest(self, s: str) -> int:
        s = list(s)
        s = list(filter(lambda x : x in "0123456789",s))
        if not s:
            return -1
        s = set(map(int,s))
        if(len(s)==1):
            return -1
        else:
            return sorted(s)[-2]