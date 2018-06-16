class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rowLen = len(board)
        if (rowLen == 0):
            return
        colLen = len(board[0])
        for i in range(rowLen):
            if (board[i][0] == 'O'):
                self.dfs(board, i, 0)
            if (board[i][colLen - 1] == 'O'):
                self.dfs(board, i, colLen - 1)

        for j in range(colLen):
            if (board[0][j] == 'O'):
                self.dfs(board, 0, j)
            if (board[rowLen - 1][j] == 'O'):
                self.dfs(board, rowLen - 1, j)

        for i in range(rowLen):
            for j in range(colLen):
                if (board[i][j] == 'O'):
                    board[i][j] = 'X'
                elif (board[i][j] == 'A'):
                    board[i][j] = 'O'

    def dfs(self, board, i, j):
        rowLen = len(board)
        colLen = len(board[0])
        if (i < 0 or i >= rowLen or j < 0 or j >= colLen):
            return
        if (board[i][j] == 'O'):
            board[i][j] = 'A'
            self.dfs(board, i + 1, j)
            self.dfs(board, i - 1, j)
            self.dfs(board, i, j + 1)
            self.dfs(board, i, j - 1)



