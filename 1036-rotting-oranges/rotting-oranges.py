from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = -1
        m, n = len(grid), len(grid[0])
        queue = deque()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh_count += 1

        if not queue and fresh_count== 0:
            return 0
            
        while queue:
            count += 1
            queue_len = len(queue)
            for idx in range(queue_len):
                x, y = queue.popleft()
                for xi, yi in directions:
                    if 0 <= x + xi < m and 0<= y + yi < n and grid[x + xi][y + yi] == 1:
                        queue.append((x + xi, y + yi))
                        grid[x + xi][y + yi] = 2
                        fresh_count -= 1
        
        if fresh_count > 0:
            return -1
        return count



