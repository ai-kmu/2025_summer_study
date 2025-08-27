# Prim
import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        
        # 방문한 노드 저장
        visited = set()
        
        # (비용, 정점 인덱스)
        min_heap = [(0, 0)]
                
        total_cost = 0
        
        while len(visited) < n:
            # 가장 비용이 적은 정점
            cost, i = heapq.heappop(min_heap)
            
            if i in visited:
                continue
            
            visited.add(i)
            total_cost += cost

            # 새로 추가된 정점 i와 다른 모든 정점들 간의 거리를 계산
            x1, y1 = points[i]
            for j in range(n):                
                if j not in visited:
                    x2, y2 = points[j]                    
                    dist = abs(x1 - x2) + abs(y1 - y2)      
                    # 연결할 수 있는 정점 추가              
                    heapq.heappush(min_heap, (dist, j))

        return total_cost