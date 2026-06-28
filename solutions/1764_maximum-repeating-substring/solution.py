class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        for i in range(1,(len(sequence)//len(word))+2):
            if word*i in sequence:
                continue
            else:
                return i-1
        