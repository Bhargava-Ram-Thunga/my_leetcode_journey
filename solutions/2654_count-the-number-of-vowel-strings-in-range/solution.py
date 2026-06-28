class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowels = "AEIOUaeiou"
        for strs in words[left:right+1]:
            if strs[0] in vowels and strs[len(strs)-1] in vowels:
                count+=1
        return count
