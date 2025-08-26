### union find로 풀기
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        parent = list(range(n))
        rank = [0]*n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b) # 각 원소가 속한 트리의 루트 찾기
            if ra == rb:
                return False
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
            return True

        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                d = abs(x1 - x2) + abs(y1 - y2)
                edges.append((d, i, j))

        edges.sort()
        res = 0
        cnt = 0
        for d, i, j in edges:
            if union(i, j):
                res += d
                cnt += 1
                if cnt == n - 1:
                    break
        return res


### heap으로 풀기
import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = [False]*n
        best = [float('inf')]*n
        best[0] = 0
        h = [(0, 0)]
        res = 0
        picked = 0
        while picked < n:
            w, u = heapq.heappop(h)
            if visited[u]:
                continue
            visited[u] = True
            res += w
            picked += 1
            x1, y1 = points[u]
            for v in range(n):
                if not visited[v]:
                    x2, y2 = points[v]
                    d = abs(x1 - x2) + abs(y1 - y2)
                    if d < best[v]:
                        best[v] = d
                        heapq.heappush(h, (d, v))
        return res
