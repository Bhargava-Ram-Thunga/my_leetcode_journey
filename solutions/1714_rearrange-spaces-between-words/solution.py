class Solution:
    def reorderSpaces(self, text: str) -> str:
        c = text.count(' ')
        words = text.split()
        n = len(words)-1
        s = 0
        if n :
            s = c//n
        se = c-(s*n)
        res = (" "*s).join(words)
        if (se):
            res += " "*se
        return res