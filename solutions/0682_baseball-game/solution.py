class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            op = operations[i]
            if((op[0] is "-" and op[1:].isdigit())or (op.isdigit())):
                res.append(int(op))
            elif (op=="C"):
                res.pop()
            elif (op=="D"):
                res.append((res[-1])*2)
            elif (op=="+"):
                res.append(res[-1]+res[-2])
            # print(res)
        return sum(res)