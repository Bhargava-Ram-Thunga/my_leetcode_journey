class Solution:
    def digitSum(self, s: str, k: int) -> str:
        temp = k
        while(len(s)>k):
            parts = [s[i:i+k] for i in range(0,len(s),k)]
            parts = list(map(lambda x:str(sum(list(map(int,list(x))))),parts))
            s = "".join(parts)
        return s