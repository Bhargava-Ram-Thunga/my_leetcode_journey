class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(li[0]+li[1] for li in tasks)