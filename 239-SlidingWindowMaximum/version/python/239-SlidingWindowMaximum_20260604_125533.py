# Last updated: 6/4/2026, 12:55:33 PM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        ans=[]
4        q=collections.deque()
5        L=R=0
6        while R<len(nums):
7            while q and nums[q[-1]]<nums[R]:
8                q.pop()
9            q.append(R)
10            if L>q[0]:
11                q.popleft()
12            if (R+1)>=k:
13                ans.append(nums[q[0]])
14                L+=1
15            R+=1
16        return ans
17