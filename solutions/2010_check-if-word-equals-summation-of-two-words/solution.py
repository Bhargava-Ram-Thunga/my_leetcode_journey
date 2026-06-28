class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        f1n = ""
        f2n = ""
        tn = ""
        for al in firstWord:
            f1n+=str(alpha.index(al))
        for al in secondWord:
            f2n+=str(alpha.index(al))
        for al in targetWord:
            tn+=str(alpha.index(al))
        return int(f1n)+int(f2n)==int(tn)