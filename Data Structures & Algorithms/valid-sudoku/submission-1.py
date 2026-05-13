class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            check_row = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in check_row:
                    return False
                
                check_row.add(board[i][j])
        
        for i in range(9):
            check_col = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in check_col:
                    return False
                
                check_col.add(board[j][i])
        
        for s in range(9):
            check_square = set()
            for i in range(3):
                for j in range(3):
                    r = (s//3) * 3 + i
                    c = (s % 3) * 3 + j
                    
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in check_square:
                        return False
                    
                    check_square.add(board[r][c])
        return True
            

