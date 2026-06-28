class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        li = []
        res = ""
        for i in range(0,len(s),k):
                li.append(s[i:i+k])
        for i in range(len(li)):
            if i%2==0:
                res+=li[i][::-1]
            else:
                res+=li[i]
        return res