class Solution:
    def reformatDate(self, date: str) -> str:
        months = ["","Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date,month,year= tuple(date.split())
        date = date[:-2]
        res = year+"-"
        if months.index(month)>9:
            res+=str(months.index(month))
        else:
            res+="0"+str(months.index(month))
        res+="-"
        if int(date)>9:
            res+=date
        else:
            res+="0"+date
        return res
        