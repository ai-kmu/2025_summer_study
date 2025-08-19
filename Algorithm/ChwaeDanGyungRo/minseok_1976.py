from collections import defaultdict
import heapq

class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:
        MOD = 10**9 + 7
    
        # 인접 리스트
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
    
        # dist: 각 교차로까지의 최단 시간을 저장
        dist = [float('inf')] * n
        # ways: 각 교차로까지 최단 시간으로 가는 방법의 수를 저장
        ways = [0] * n
    
        # 시작점 초기화
        dist[0] = 0
        ways[0] = 1
    
        # 우선순위 큐: (소요 시간, 교차로 번호)로 저장   
        pq = [(0, 0)]
    
        while pq:   
            d, u = heapq.heappop(pq)
    
            if d > dist[u]:
                continue
        
            for v, time in graph[u]:
                if dist[u] + time < dist[v]:   
                    dist[v] = dist[u] + time   
                    ways[v] = ways[u]   
                    heapq.heappush(pq, (dist[v], v))
                elif dist[u] + time == dist[v]:      
                    ways[v] = (ways[v] + ways[u]) % MOD
    
        return ways[n - 1]