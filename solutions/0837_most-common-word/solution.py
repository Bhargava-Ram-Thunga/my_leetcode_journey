class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        temp = ""
        for i in range(len(paragraph)):
            if paragraph[i].isalpha() or paragraph[i] == " ":
                temp += paragraph[i]
            elif paragraph[i] == ",":
                temp += " "
            
        temp = temp.lower()
        for string in sorted(banned)[::-1]:
            temp = temp.replace(string,"")
        temp = temp.split()
        # return temp
        return max(temp,key = lambda x : temp.count(x))
