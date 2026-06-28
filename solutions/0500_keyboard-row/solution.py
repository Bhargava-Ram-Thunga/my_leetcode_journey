class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            if set(word).issubset(set("asdfghjklASDFGHJKL")) or set(word).issubset(set("qwertyuiopQWERTYUIOP")) or set(word).issubset(set("zxcvbnmZXCVBNM")):
                res.append(word)
        return res
