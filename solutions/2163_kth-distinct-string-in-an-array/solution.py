class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for c in arr:
            if arr.count(c)==1:
                k-=1
                if k==0:
                    return c
        return ""
