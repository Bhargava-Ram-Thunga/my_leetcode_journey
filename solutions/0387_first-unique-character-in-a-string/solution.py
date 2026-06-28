class Solution:
    def firstUniqChar(self, s: str) -> int:
        charSet = set(s)
        li = []
        for c in charSet:
            if s.count(c) == 1 :
                li.append(s.index(c))
        if li:
            return min(li)
        return -1