class Solution(object):
    def highestPeak(self, isWater):
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        n,m = len(isWater),len(isWater[0])
        vis = [[0]* m for i in range(n)]
        res = [[0]* m for i in range(n)]
        stk = []
        for i in range(n):
            for j in range(m):
                if isWater[i][j]==1:
                    vis[i][j] = 1
                    stk.append([i,j])
        while stk:
            cx,cy = stk.pop(0)
            for k in range(4):
                nx,ny = cx + dx[k] ,cy + dy[k]
                if 0 <= nx < n and 0 <= ny < m and vis[nx][ny] == 0:
                    res[nx][ny] = res[cx][cy]+1
                    vis[nx][ny] = 1
                    stk.append([nx,ny])
        return res