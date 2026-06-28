class Solution:
    def findLatestTime(self, s: str) -> str:
        H,M = s.split(":")
        # H
        if H.count("?")>0:
            if H == "??" :
                H = "11"
            elif H[0]=="?":
                if int(H[1]) <2:
                    H = "1"+H[1]
                else:
                    H = "0"+H[1]
            elif H[1] == "?":
                if int(H[0]) == 0:
                    H = H[0] + "9"
                elif int(H[0]) ==1:
                    H = H[0]+"1"
        # M
        if M.count("?")>0:
            if M[0] == "?":
                M = "5"+M[1]
            if M[1] == "?":
                M = M[0] +"9"
        return f"{H}:{M}"
        

        