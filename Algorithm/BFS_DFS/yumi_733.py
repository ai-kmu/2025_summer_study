from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        before_color = image[sr][sc]
        if before_color == color:  # 이미 같은 색이면 그대로 반환
            return image
        
        rows, cols = len(image), len(image[0])
        queue = deque()   # 탐색할 좌표들을 담을 빈 큐 생성.
        queue.append((sr, sc))   # 시작 좌표를 큐에 넣음 (탐색 시작점).
        
        while queue:
            r, c = queue.popleft()   # — 큐에서 다음 좌표를 꺼냄(먼저 넣은 것이 먼저 나옴 — BFS).
            if image[r][c] == before_color:
                image[r][c] = color
                
                # 상, 하, 좌, 우 탐색
                if r-1 >= 0: 
                    queue.append((r-1, c))
                if r+1 < rows: 
                    queue.append((r+1, c))
                if c-1 >= 0: 
                    queue.append((r, c-1))
                if c+1 < cols: 
                    queue.append((r, c+1))
        
        return image
