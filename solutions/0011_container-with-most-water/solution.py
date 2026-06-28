class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 2:
            return min(height)
        s = 0
        e = len(height)-1
        res = []
        for i in range(len(height)):
            res.append(min(height[s],height[e])*(e-s))
            if height[e]>=height[s]:
                s+=1
            else:
                e-=1
        return max(res)
