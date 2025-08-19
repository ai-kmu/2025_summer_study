import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
    # 그래프 만들기 (인접 리스트)
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))  # u → v (가중치 w)

        # 다익스트라: (걸린시간, 노드)
        heap = [(0, k)]
        dist = {}

        while heap:
            time, node = heapq.heappop(heap)
            if node in dist:  # 이미 최단 거리 확정된 노드면 패스
                continue
            dist[node] = time
            for nei, w in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (time + w, nei))

        # 모든 노드가 도달했는지 확인
        if len(dist) != n:
            return -1
        return max(dist.values())

            
