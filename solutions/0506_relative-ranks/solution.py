class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = sorted(score)[::-1]
        di = {}
        for i in range(len(temp)):
            if i==0:
                di[temp[i]] = "Gold Medal"
            elif i==1:
                di[temp[i]] ="Silver Medal"
            elif i==2:
                di[temp[i]] = "Bronze Medal"
            else:
                di[temp[i]] = str(i+1)
        for i in range(len(score)):
            score[i] = di[score[i]]
        return score
