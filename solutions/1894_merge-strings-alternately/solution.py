class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res= ""
        for i in range(len(word1)):
            if i==len(word1)-1:
                res+=word1[i]
                res+=word2[i:]
                break
            elif i==len(word2)-1:
                res+=word1[i]
                res+=word2[i:]
                res+=word1[i+1:]
                break
            else:
                res+=word1[i]
                res+=word2[i]
        return res

        