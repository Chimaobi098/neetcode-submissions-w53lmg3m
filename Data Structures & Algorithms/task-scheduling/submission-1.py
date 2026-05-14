class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_map = {}

        for task in tasks:
            task_map[task] = 1 + task_map.get(task, 0)

        maxHeap = [-count for count in task_map.values()]

        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # stores [count  time]

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
            # if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                    heapq.heappush(maxHeap, q.popleft()[0])
        return time
        