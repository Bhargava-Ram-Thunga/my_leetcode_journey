class Solution(object):
    def finalValueAfterOperations(self, operations):
        count = 0
        for operation in operations:
            if "++" in operation:
                count+=1
            elif "--" in operation:
                count-=1
        return count
        