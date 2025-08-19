class Solution:
    def networkDelayTime(self, times, n, k): # k = start, n = num of nodes
        queue = [(k, k, 0)]
        max_time = 0
        visited_node = set()
        while queue:
            now = min(queue, key=lambda x: x[2])
            queue.remove(now)
            now_start = now[1]
            if now_start in visited_node:
                continue
            visited_node.add(now_start)
            max_time = max(max_time, now[2])
            next_list = [(x[0], x[1], x[2]+now[2]) for x in times if x[0] == now_start]
            for nxt in next_list:
                queue.append(nxt)
        if len(visited_node) != n:
            return -1
        return max_time
