class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        count = 0
        board_t = list(map(list,zip(*board)))
        R_pos = [-1,-1]
        for i,row in enumerate(board):
            if "R" in row:
                R_pos = [i,row.index("R")]
                break
        i,j = R_pos
        R_row = "".join(board[i]).replace(".","")
        R_col = "".join(board_t[j]).replace(".","")
        i = R_row.index("R")
        j = R_col.index("R")
        # print(R_row[i-2:i+2])
        # print(R_col[j-1:j+2])
        if i > 0:
            R_row = R_row[i-1:i+2]
        else:
            R_row = R_row[0:2]
        if j > 0:
            R_col = R_col[j-1:j+2]
        else:
            R_col = R_col[0:2]
        # print(R_row,R_col)
        return R_row.count("p")+R_col.count("p")
        
