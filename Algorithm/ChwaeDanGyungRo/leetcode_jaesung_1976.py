import heapq

class Solution:
    def countPaths(self, n, roads):
        MOD = 10**9 + 7

        graph = [[] for _ in range(n)]
        for start, end, w in roads:
            graph[start].append((end, w))
            graph[end].append((start, w))

        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        pq = [(0, 0)]  # (time, node)

        while pq:
            t, start = heapq.heappop(pq)
            if t > dist[start]:
                continue

            for end, w in graph[start]:
                new_t = t + w
                if new_t < dist[end]:
                    dist[end] = new_t
                    ways[end] = ways[start]
                    heapq.heappush(pq, (new_t, end))
                elif new_t == dist[end]:
                    ways[end] = (ways[end] + ways[start]) % MOD

        return ways[n - 1]
