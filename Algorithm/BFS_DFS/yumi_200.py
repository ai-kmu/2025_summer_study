from collections import deque

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":  # 땅 발견
                    islands += 1
                    queue = deque()
                    queue.append((r, c))
                    
                    while queue:
                        x, y = queue.popleft()   # 탐색할 좌표 꺼내기.
                        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
                            grid[x][y] = "0"  # 방문 처리 (물로 바꿔버림)
                            queue.append((x-1, y))  # 위
                            queue.append((x+1, y))  # 아래
                            queue.append((x, y-1))  # 왼쪽
                            queue.append((x, y+1))  # 오른쪽
        return islands
