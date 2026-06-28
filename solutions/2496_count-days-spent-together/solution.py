from datetime import datetime
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a1 = datetime.strptime(f"{2025}-{arriveAlice}",f"%Y-%m-%d")
        d1 = datetime.strptime(f"{2025}-{leaveAlice}",f"%Y-%m-%d")

        a2 = datetime.strptime(f"{2025}-{arriveBob}",f"%Y-%m-%d")
        d2 = datetime.strptime(f"{2025}-{leaveBob}",f"%Y-%m-%d")

        overlap_start = max(a1,a2)
        overlap_end = min(d1,d2)
        if(overlap_start <= overlap_end):
            return (overlap_end - overlap_start).days +1
        return 0