from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        pos_row = [-1, 0 ,1, 0]
        pos_col = [0, 1, 0, -1]

        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if visited[r][c] == True or grid[r][c] == "0":
                    continue
                q = deque()
                q.append((r, c))
                visited[r][c] = True
                # BFS
                while q:
                    cur_row, cur_col = q.popleft()
                    for i in range(4):
                        target_row, target_col = cur_row + pos_row[i], cur_col + pos_col[i]
                        if target_row < 0 or target_row >= len(grid) or target_col < 0 or target_col >= len(grid[0]):
                            continue
                        if grid[target_row][target_col] == "0":
                            continue
                        if visited[target_row][target_col] == True:
                            continue
                        q.append((target_row, target_col))
                        visited[target_row][target_col] = True
                count += 1
        return count
                