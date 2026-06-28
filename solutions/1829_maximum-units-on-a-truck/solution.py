class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes,key = lambda x : [-x[1],-x[0]])
        temp = truckSize
        res = 0
        for boxes,units in boxTypes:
            if(boxes < temp):
                res += boxes*units
                temp-=boxes
            else:
                res += temp*units
                return res
        return res