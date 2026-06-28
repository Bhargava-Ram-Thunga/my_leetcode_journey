class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        chars = set(s)
        li = []
        for char in chars:
            li.append(s.count(char))
        return len(set(li)) == 1
