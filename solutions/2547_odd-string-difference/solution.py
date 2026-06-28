class Solution:
    def oddString(self, words: List[str]) -> str:
        for i in range(1,len(words)-1):
            temp = list(map(lambda x :ord(x[i])-ord(x[i-1]),words))
            print(temp)
            if(len(set(temp)) >1):
                c = Counter(temp)
                u = next(k for k, v in c.items() if v == 1)
                return words[temp.index(u)]
                print(temp.index(u))
                print(words[temp.index(u)])
                break
        return ""