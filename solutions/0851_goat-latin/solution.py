class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        res = ""
        for i in range(len(words)):
            word = words[i]
            if word[0] in "aeiouAEIOU" :
                res += word+"ma"+("a"*(i+1))
            else:
                res += word[1:]+word[0]+"ma"+("a"*(i+1))
            if i != len(words)-1:
                    res += " "
        return res

                

