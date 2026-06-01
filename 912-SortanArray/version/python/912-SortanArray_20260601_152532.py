# Last updated: 6/1/2026, 3:25:32 PM
1import heapq
2class Solution:
3    def sortArray(self, nums: List[int]) -> List[int]:
4        if not nums:
5            return
6        heapq.heapify(nums)
7        ans=[]
8        for i in range(len(nums)):
9            a=heapq.heappop(nums)
10            ans.append(a)
11        return ans