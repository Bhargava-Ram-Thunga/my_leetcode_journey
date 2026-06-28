class Solution(object):
    def checkIfPangram(self, sentence):
        for alpha in range(ord("a"),ord("z")+1):
            if chr(alpha) not in sentence:
                return False
        return True
        