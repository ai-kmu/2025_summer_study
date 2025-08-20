from typing import List
import heapq
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        g = defaultdict(list)
        for u, v, t in roads:
            g[u].append((v, t))
            g[v].append((u, t))  # 양방향

        INF = 10**18
        dist = [INF] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]  # (시간, 노드)
        while pq:
            t, u = heapq.heappop(pq)
            if t > dist[u]:
                continue
            for v, w in g[u]:
                nt = t + w
                if nt < dist[v]:
                    dist[v] = nt
                    ways[v] = ways[u]
                    heapq.heappush(pq, (nt, v))
                elif nt == dist[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD

        return ways[n-1] % MOD