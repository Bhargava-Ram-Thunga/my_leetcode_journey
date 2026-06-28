class Solution(object):
    def countSeniors(self, details):
        count =0
        for det in details:
            if int(det[11:13])>60:
                count+=1
        return count
        