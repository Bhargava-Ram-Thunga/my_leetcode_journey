class Solution:
    def removeDigit(self, num: str, digit: str) -> str:
        li = []
        for i in range(len(num)):
            if num[i] == digit:
                li.append(int(num[:i]+num[i+1:]))
        return str(sorted(li)[-1])