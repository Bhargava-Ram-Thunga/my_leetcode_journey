class Solution(object):
    def squareIsWhite(self, coordinates):
        even = "aceg"
        odd = "bdfh"
        co = list(coordinates)
        if co[0] in even:
            if int(co[1])%2==0:
                return True
            else:
                return False
        else:
            if int(co[1])%2==0:
                return False
            else:
                return True
        