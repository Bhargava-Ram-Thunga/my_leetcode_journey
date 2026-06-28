class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        test = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i]-test>0:
                test+=1
        return test