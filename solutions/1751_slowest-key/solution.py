class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        temp = []
        for i in range(len(releaseTimes)):
            if i ==0 :
                temp.append(releaseTimes[0])
            else:
                temp.append(releaseTimes[i]-releaseTimes[i-1])
        slow = max(temp)
        temp2 = []
        if temp.count(slow) ==1 :
            return keysPressed[temp.index(slow)]
            # pass
        else:
            for t in range(len(temp)):
                if (temp[t]==slow):
                    temp2.append(keysPressed[t])
        # print(temp)
        # print(temp2)
        # print(slow)
        return max(temp2)

