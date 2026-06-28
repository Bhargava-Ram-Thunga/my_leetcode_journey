class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        count=0
        for emp in hours:
            if emp>=target:
                count+=1
        return count
        