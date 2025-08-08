from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        result = 0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1":
                    queue = deque()
                    queue.append((i, j))
                    grid[i][j] = "0"
                    while queue:
                        r, c = queue.popleft()
                        next_r = r+1
                        next_c = c+1
                        prev_r = r-1
                        prev_c = c-1
                        if next_r < row_len and grid[next_r][c] == "1":
                            queue.append((next_r, c))
                            grid[next_r][c] = "0"
                        if next_c < col_len and grid[r][next_c] == "1":
                            queue.append((r, next_c))
                            grid[r][next_c] = "0"
                        if prev_r > -1 and grid[prev_r][c] == "1":
                            queue.append((prev_r, c))
                            grid[prev_r][c] = "0"
                        if prev_c > -1 and grid[r][prev_c] == "1":
                            queue.append((r, prev_c))
                            grid[r][prev_c] = "0"
                    result += 1

        return result
