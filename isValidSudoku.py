class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        lie = list()
        for i in range(len(board)):
            lie.append(map(lambda x:x[i], board))
        blk = list()
        for d in range(3):
            for k in range(3):
                tmp = list()
                for i in range(3):
                    for j in range(3):
                        tmp.append(board[i+d*3][j+k*3])
                blk.append(tmp)
        for tojdg in board+lie+blk:
            tmp = list()
            for c in tojdg:
                if c != '.' and c in tmp:
                    return False
                else:
                    tmp.append(c)
        return True
