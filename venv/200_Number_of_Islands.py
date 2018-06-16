class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rowLen = len(grid)
        if (rowLen == 0):
            return 0;
        colLen = len(grid[0])
        numOfIsland = 0
        rowLen = len(grid)
        for i in range(rowLen):
            for j in range(colLen):
                if (grid[i][j] == '1'):
                    numOfIsland += 1
                    self.dfs(grid, i, j)
        return numOfIsland

    def dfs(self, grid, i, j):
        rowLen = len(grid)
        colLen = len(grid[0])
        if (i < 0 or j < 0 or i >= rowLen or j >= colLen or grid[i][j] == '0'):
            return None
        grid[i][j] = '0'
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)



