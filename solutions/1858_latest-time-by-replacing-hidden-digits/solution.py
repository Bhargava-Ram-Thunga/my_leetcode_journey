class Solution:
    def maximumTime(self, time: str) -> str:
        h,m= time.split(":")
        if(h.count("?") == 2):
            h = "23"
        if (m.count("?") == 2):
            m  = "59"
        h = list(h)
        m = list(m)
        if('?' in h):
            if(h[0].isdigit()):
                if(int(h[0]) <2):
                    h[1] = '9'
                else:
                    h[1] = '3'
            else:
                if(int(h[1]) <= 3):
                    h[0] = '2'
                else:
                    h[0] = '1'
        
        if('?' in m):
            if(m[0].isdigit()):
                m[1] = '9'
            else:
                m[0] = '5'
        
        h = "".join(h)
        m = "".join(m)
        # print(h)
        # print(m)
        return f"{h}:{m}"