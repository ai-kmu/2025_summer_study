import heapq

class Solution(object):
    def countPaths(self, n, roads):
        MOD = 10**9 + 7
        
        # 그래프 생성 (양방향)
        graph = {i: [] for i in range(n)}
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # 다익스트라
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        heap = [(0, 0)]  # (시간, 노드)
        
        while heap:
            time, node = heapq.heappop(heap)
            
            # 이미 더 짧은 거리로 방문했다면 패스
            if time > dist[node]:
                continue
            
            for nei, w in graph[node]:
                new_time = time + w
                
                # 더 짧은 경로 발견
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    ways[nei] = ways[node]
                    heapq.heappush(heap, (new_time, nei))
                
                # 같은 최단 경로 발견
                elif new_time == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD
        
        return ways[n-1] % MOD
            
