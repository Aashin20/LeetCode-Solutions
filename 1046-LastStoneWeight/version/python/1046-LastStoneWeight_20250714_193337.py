# Last updated: 7/14/2025, 7:33:37 PM
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)
        while len(stones)>1:
            x=-heapq.heappop(stones)
            y=-heapq.heappop(stones)
            if x!=y:
                heapq.heappush(stones,-(x - y))
            else:
                continue
        return -stones[0] if stones else 0
        