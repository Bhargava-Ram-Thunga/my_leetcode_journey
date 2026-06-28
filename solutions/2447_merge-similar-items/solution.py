class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        i1 = dict(items1)
        i2 = dict(items2)
        d2 = i2.keys() - i1.keys()
        res = []
        for val,weight in i1.items():
            if(val in i2):
                res.append([val,weight+i2[val]])
            else:
                res.append([val,weight])
        for key in d2:
            res.append([key,i2[key]])
        return sorted(res)