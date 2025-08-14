from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        문제: '1'(육지)과 '0'(물)로 이루어진 격자에서,
             상/하/좌/우로 연결된 '1' 묶음(섬)의 개수를 구한다.
        아이디어: 격자를 그래프로 보고, '1'을 만나면 DFS로 연결된 '1'을 모두 '0'으로 바꿔
                 해당 섬을 한 번에 방문 처리(플러드-필)한다.
        """

        # 1) 예외 처리: 빈 격자면 섬 0개
        if not grid:
            return 0

        # 2) 격자 크기
        m, n = len(grid), len(grid[0])

        # 3) DFS: (r, c)에서 시작해 같은 섬에 속한 모든 칸을 '0'으로 바꿈(방문 표시)
        def dfs(r: int, c: int) -> None:
            # (a) 범위 밖이거나, 육지가 아니면 즉시 종료
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != "1":
                return

            # (b) 현재 칸 방문 처리: '1' -> '0' (in-place 마킹으로 재방문/중복 카운트 방지)
            grid[r][c] = "0"

            # (c) 상/하/좌/우로 확장(대각선은 포함하지 않음)
            dfs(r + 1, c)  # 아래
            dfs(r - 1, c)  # 위
            dfs(r, c + 1)  # 오른쪽
            dfs(r, c - 1)  # 왼쪽

        # 4) 모든 칸을 순회하며 아직 물로 바뀌지 않은 '1'을 섬의 시작점으로 삼아 DFS 수행
        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":  # 새 섬 발견
                    answer += 1           # 섬 개수 +1
                    dfs(i, j)          # 연결된 '1'을 모두 '0'으로 바꿔 같은 섬 재발견 방지

        # 5) 최종 섬 개수 반환
        return answer