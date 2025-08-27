class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = set()
        heap = [(0, 0)]  # (비용, 시작점) -> 처음엔 0번 노드 비용 0으로 시작
        total_cost = 0

        while len(visited) < n:
            cost, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            total_cost += cost

            # 현재 점 u에서 다른 점 v까지의 거리 계산해서 후보에 넣기
            x1, y1 = points[u]
            for v in range(n):
                if v not in visited:
                    x2, y2 = points[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(heap, (dist, v))

        return total_cost
