class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            word = list(words[i])
            for char in word:
                if char not in allowed:
                    count+=1
                    break
        return len(words)-count