class Solution(object):
    def mostWordsFound(self, sentences):
        count = 0
        for sentence in sentences:
            count = max(count,sentence.count(" ")+1)
        return count