class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictRansom = Counter(ransomNote)
        for key in dictRansom:
            if dictRansom[key] > magazine.count(key):
                return False
        return True