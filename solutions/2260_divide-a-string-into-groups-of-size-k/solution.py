class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = 0
        if(len(s)%k!=0):
            n = (((len(s)//k)+1)*k)-len(s)
        s += fill*n
        return [s[i:i+k] for i in range(0,len(s),k)]
