class Solution:
    def stringSequence(self, target: str) -> List[str]:
        s = "abcdefghijklmnopqrstuvwxyz"
        temp = ""
        res = []
        for i in range(len(target)):
            for j in range(s.index(target[i])+1):
                res.append(temp+s[j])
            temp += target[i]
        return res
