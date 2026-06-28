class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        temp = []
        for val in tokens:
            if val in "+-*/":
                num1 = int(temp.pop())
                num2 = int(temp.pop())
                if val == "+":
                    temp.append(num1+num2)
                elif val == "*":
                    temp.append(num1*num2)
                elif val == "-":
                    temp.append(num2-num1)
                elif val == "/":
                    temp.append(int(num2/num1))
            else:
                temp.append(val)
        return int(temp[0])