class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        vowelOrder = ""
        for c in s:
            if c in vowels:
                vowelOrder+=c
        vowelOrder = vowelOrder[::-1]
        temp=0
        res = ""
        for c in s:
            if c in vowels:
                res+=vowelOrder[temp]
                temp+=1
            else:
                res+=c
        return res