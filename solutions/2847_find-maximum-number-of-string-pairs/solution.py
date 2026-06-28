class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)-1):
            if words[i][::-1] in words[i+1:]:
                count+=1
        return count