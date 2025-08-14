from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        문제:
        - image[r][c]는 픽셀 색상(정수).
        - 시작 좌표 (sr, sc)에서 출발해, 시작 픽셀과 '같은 색'이면서
          상/하/좌/우(4-이웃)로 연결된 모든 픽셀을 새 색 color로 바꾼 후 image를 반환.

        핵심 아이디어(Flood Fill):
        - 시작점의 원래 색(original_color)을 기준으로 DFS/BFS로 4-이웃을 확장.
        - 방문 즉시 색을 color로 변경하여 재방문을 방지(in-place 마킹).
        """

        original_color = image[sr][sc]          # 시작 픽셀의 '원래 색' 저장
        if original_color == color:             # 이미 목표 색이면 더 바꿀 필요 없음 (무한루프 방지)
            return image
        
        m, n = len(image), len(image[0])        # 격자 크기

        def dfs(r: int, c: int) -> None:
            # 1) 경계 체크: 격자 밖이면 중단
            # 2) 색상 체크: 원래 색과 다르면(=채울 대상 아님) 중단
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != original_color:
                return

            image[r][c] = color                 # 방문 즉시 새 색으로 변경(재방문/중복 방지)

            # 4방향으로 확장(대각선은 포함하지 않음)
            dfs(r + 1, c)                       # 아래
            dfs(r - 1, c)                       # 위
            dfs(r, c + 1)                       # 오른쪽
            dfs(r, c - 1)                       # 왼쪽
        
        dfs(sr, sc)                             # 시작점에서 플러드-필 수행
        return image                            # 변경된 이미지 반환