from typing import List
import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프 인접 리스트
        g = defaultdict(list)
        for u, v, w in times:
            g[u].append((v, w))

        INF = 10**18
        dist = [INF] * (n + 1)
        dist[k] = 0

        # 최소 힙
        pq = [(0, k)]
        while pq:
            t, u = heapq.heappop(pq)
            if t > dist[u]:
                continue
            for v, w in g[u]:
                nt = t + w
                if nt < dist[v]:
                    dist[v] = nt
                    heapq.heappush(pq, (nt, v))

        ans = max(dist[1:])  # 노드 라벨은 1 ... n
        return -1 if ans == INF else ans