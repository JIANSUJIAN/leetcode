#
# @lc app=leetcode id=348 lang=python3
#
# [348] Design Tic-Tac-Toe
#

# @lc code=start

# Approach 1: Brute Force
# class TicTacToe:

#     def __init__(self, n: int):
        
#         self.board = [[0] * n for _ in range(n)]
#         self.n = n

#     def move(self, row: int, col: int, player: int) -> int:

#         self.board[row][col] = player

#         if (self.checkRow(row, player) or 
#             self.checkCol(col, player) or
#             (row == col and self.checkDiagnol(player)) or
#             (col == self.n - row - 1 and self.checkAntiDiagnol(player))):
#             return player

#         return 0

#     def checkRow(self, row, player):
#         for col in range(self.n):
#             if self.board[row][col] != player:
#                 return False
            
#         return True

#     def checkCol(self, col, player):
#         for row in range(self.n):
#             if self.board[row][col] != player:
#                 return False
        
#         return True
    
#     def checkDiagnol(self, player):
#         for i in range(self.n):
#             if self.board[i][i] != player:
#                 return False
#         return True
    
#     def checkAntiDiagnol(self, player):
#         for i in range(self.n):
#             if self.board[i][self.n - i - 1] != player:
#                 return False
#         return True


# Approch 2: Optimized Approach
class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:

        current_player = 1 if player == 1 else -1

        self.rows[row] += current_player
        self.cols[col] += current_player

        if row == col:
            self.diagonal += current_player
        
        if col == (self.n - row - 1):
            self.anti_diagonal += current_player
        
        if (abs(self.rows[row]) == self.n or 
            abs(self.cols[col]) == self.n or 
            abs(self.diagonal) == self.n or 
            abs(self.anti_diagonal) == self.n):
            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
# @lc code=end

