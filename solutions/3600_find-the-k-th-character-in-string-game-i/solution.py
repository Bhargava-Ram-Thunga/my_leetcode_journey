class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while(len(word) < k):
            word += "".join(map(lambda x : 'a' if x=='z' else chr(ord(x) + 1),word))
        return word[k-1]