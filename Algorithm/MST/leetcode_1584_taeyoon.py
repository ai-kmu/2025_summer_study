class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        in_mst = [False] * n
        INF = 10**18
        minDist = [INF] * n
        minDist[0] = 0
        total = 0

        for _ in range(n):
            u = -1
            best = INF
            for i in range(n):
                if not in_mst[i] and minDist[i] < best:
                    best = minDist[i]
                    u = i

            in_mst[u] = True
            total += best

            xu, yu = points[u]
            for v in range(n):
                if not in_mst[v]:
                    xv, yv = points[v]
                    w = abs(xu - xv) + abs(yu - yv)
                    if w < minDist[v]:
                        minDist[v] = w

        return total
