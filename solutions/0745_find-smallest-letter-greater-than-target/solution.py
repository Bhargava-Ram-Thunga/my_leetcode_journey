class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(ord(target)+1,ord("z")+1):
            if chr(i) in letters:
                return chr(i)
        return letters[0]