# Last updated: 7/11/2025, 11:55:51 PM
import heapq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free = list(range(n))         
        heapq.heapify(free)

        busy = []                     
        count = [0] * n

        for s, e in meetings:
            while busy and busy[0][0] <= s:
                _, r = heapq.heappop(busy)
                heapq.heappush(free, r)

            if free:
                r = heapq.heappop(free)
                new_end = e
            else:
                end_time, r = heapq.heappop(busy)
                new_end = end_time + (e - s)
            heapq.heappush(busy, (new_end, r))
            count[r] += 1

        return max(range(n), key=count.__getitem__)