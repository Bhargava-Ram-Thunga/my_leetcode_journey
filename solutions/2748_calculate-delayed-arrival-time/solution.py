class Solution:
    def findDelayedArrivalTime(self, arr: int, delay: int) -> int:
        return (arr+delay)%24