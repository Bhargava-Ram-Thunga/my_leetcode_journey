class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            for char in word:
                if word.count(char)>chars.count(char):
                    break
            else:
                count+=len(word)
        return count