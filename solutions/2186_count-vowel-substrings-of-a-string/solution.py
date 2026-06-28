class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = "aeiou"
        count = 0
        for i in range(len(word)):
            for j in range(len(word)):
                if set(word[i:j+1])==set(vowels):
                    count+=1
        return count
            