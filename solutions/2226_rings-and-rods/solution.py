class Solution:
    def countPoints(self, rings: str) -> int:
        li = [""]*(10)
        for i in range(1,len(rings),2):
            index = int(rings[i])
            char = rings[i-1]
            if char not in li[index]:
                li[index] += char
        count = 0
        for string in li:
            if len(string) == 3:
                count+=1
        return count