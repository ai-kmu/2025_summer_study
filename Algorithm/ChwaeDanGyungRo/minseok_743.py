from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # 인접 리스트
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        # 각 노드까지의 최단 거리를 저장할 딕셔너리        
        dist = {}
        # 우선순위 큐 사용, (소요 시간, 노드) 형태로 저장
        pq = [(0, k)]
        # 다익스트라
        while pq:        
            time, node = heapq.heappop(pq)        
            if node in dist:
                continue        
            dist[node] = time        
            for v, w in graph[node]:        
                alt = time + w        
                heapq.heappush(pq, (alt, v))                
        if len(dist) == n:                
            return max(dist.values())
        else:        
            return -1