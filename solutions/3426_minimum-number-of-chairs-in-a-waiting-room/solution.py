class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        li = []
        for i in range(len(s)):
            if s[i] == "E":
                count+=1
            else:
                count-=1
            li.append(count)
        return max(li)