class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        for i in range(len(words)):
            temp = "".join(words[:i+1])
            if s==temp:
                return True
        return False