from datetime import date
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = list(map(int,date1.split("-")))
        date2 = list(map(int,date2.split("-")))
        d1 = date(date1[0],date1[1],date1[2])
        d2 = date(date2[0],date2[1],date2[2])
        return abs((d2-d1).days)