class Solution(object):
    def countServers(self, grid):
        n , m = len(grid),len(grid[0])
        row_count = [0]*n
        col_count = [0]*m
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    row_count[i] += 1
                    col_count[j] += 1
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] and max(row_count[i],col_count[j]) > 1:
                    res += 1
        return res