class Solution(object):
    def reversePrefix(self, word, ch):
        res = ""
        for i in range(word.find(ch),-1,-1):
            res+=word[i]
        res+=word[word.find(ch)+1:]
        return res

        