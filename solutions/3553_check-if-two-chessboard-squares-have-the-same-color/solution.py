class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        chessBoard = [
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
        ]
        return chessBoard[ord(coordinate1[0])-97][int(coordinate1[1])-1] == chessBoard[ord(coordinate2[0])-97][int(coordinate2[1])-1]