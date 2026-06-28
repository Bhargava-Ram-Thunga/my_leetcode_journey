class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while(part in s):
            start_ind = s.find(part)
            end_ind = start_ind+len(part)
            s = s[:start_ind]+s[end_ind:]
        return s