# Last updated: 7/14/2025, 7:43:04 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        popped=0
        while k>0:
            popped=heapq.heappop(nums)
            k-=1
        return -popped