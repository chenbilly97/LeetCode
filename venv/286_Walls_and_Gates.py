class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        rowLen = len(rooms)
        if (rowLen == 0):
            return
        colLen = len(rooms[0])
        q = []
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(rowLen):
            for j in range(colLen):
                if (rooms[i][j] == 0):
                    q.append((i, j))

        while (not len(q) == 0):
            point = q.pop()
            row, col = point[0], point[1]
            for k in range(len(direction)):
                r = row + direction[k][0]
                c = col + direction[k][1]
                if (r < 0 or r >= rowLen or c < 0 or c >= colLen):
                    continue
                if (rooms[r][c] > rooms[row][col] + 1):
                    rooms[r][c] = rooms[row][col] + 1
                    q.append((r, c))







