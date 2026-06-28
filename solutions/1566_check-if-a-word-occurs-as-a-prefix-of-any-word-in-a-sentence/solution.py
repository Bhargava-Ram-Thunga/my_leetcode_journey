class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        string_li = sentence.split()
        for i in range(len(string_li)):
            if string_li[i].startswith(searchWord):
                return i+1
        return -1