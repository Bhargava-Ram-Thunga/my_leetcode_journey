class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        i = abs(commands.count("DOWN")-commands.count("UP"))
        j = abs(commands.count("LEFT")-commands.count("RIGHT"))
        return (i*n)+j
        