class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_len = len(image)
        col_len = len(image[0])
        value = image[sr][sc]
        if value == color: return image
        queue = deque()
        queue.append((sr, sc))
        image[sr][sc] = color
        while queue:
            r, c = queue.popleft()
            next_r = r+1
            next_c = c+1
            prev_r = r-1
            prev_c = c-1
            if next_r < row_len and image[next_r][c] == value:
                queue.append((next_r, c))
                image[next_r][c] = color
            if next_c < col_len and image[r][next_c] == value:
                queue.append((r, next_c))
                image[r][next_c] = color
            if prev_r > -1 and image[prev_r][c] == value:
                queue.append((prev_r, c))
                image[prev_r][c] = color
            if prev_c > -1 and image[r][prev_c] == value:
                queue.append((r, prev_c))
                image[r][prev_c] = color
    
        return image
