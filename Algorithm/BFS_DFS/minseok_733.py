from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        current_color = image[sr][sc]
        # 만약 image[sr][sc]가 color와 같다면 더이상 진행할 수가 없음
        if current_color == color:
            return image
        # 시작 위치 color로 바꾸기
        image[sr][sc] = color
        # 방문한 위치 체크
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        # 방문해야 하는 위치 저장
        q = deque()
        # 시작 위치 저장
        q.append((sr, sc))
        # 시작 위치 방문했다고 체크
        visited[sr][sc] = True
        
        # row, col 각각 위, 오, 아, 왼 순으로
        pos_row = [-1, 0, 1, 0]
        pos_col = [0, 1, 0, -1]

        # BFS
        while q:
            cur_row, cur_col = q.popleft()
            for i in range(4):
                target_row, target_col = cur_row + pos_row[i], cur_col + pos_col[i]
                # 목표 위치가 list out of range이면 continue
                if target_row >= len(image) or target_row < 0 or target_col >= len(image[0]) or target_col < 0:
                    continue
                # 이미 방문한 위치면 continue
                if visited[target_row][target_col] == True:
                    continue
                # 같은 color가 아니라면 continue
                if image[target_row][target_col] != current_color:
                    continue
                # 같은 color라면
                q.append((target_row, target_col))
                visited[target_row][target_col] = True
                image[target_row][target_col] = color
        return image