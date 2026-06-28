class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        temp = []
        ind  = []
        for v in list1 :
            if(v in list2):
                temp.append(v)
                ind.append(list1.index(v)+list2.index(v))
        mi = min(ind)
        res = []
        for i in range(len(ind)):
            if mi == ind[i]:
                res.append(temp[i])
        return res