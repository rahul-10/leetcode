from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] in ["0", "-1"]:
                    continue

                queue.append((i, j))
                count += 1
                while len(queue):
                    x, y = queue.popleft()
                    if x+1 < m and grid[x+1][y] == '1':
                        grid[x+1][y] = '-1'
                        queue.append((x+1, y))
                    if y+1 < n and grid[x][y+1] == '1':
                        grid[x][y+1] = '-1'
                        queue.append((x, y+1))
                    if x-1 >= 0 and grid[x-1][y] == '1':
                        grid[x-1][y] = '-1'
                        queue.append((x-1, y))
                    if y-1 >= 0  and grid[x][y-1] == '1':
                        grid[x][y-1] = '-1'
                        queue.append((x, y-1))
                    
        return count
                
        