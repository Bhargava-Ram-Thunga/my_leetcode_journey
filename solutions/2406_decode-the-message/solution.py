class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        li = []
        res = ""
        for char in key:
            if char != " " and char not in li:
                li.append(char)
        for char in message:
            if char==" ":
                res+=" "
            elif char in key:
                res+= chr(li.index(char)+97)
        return res