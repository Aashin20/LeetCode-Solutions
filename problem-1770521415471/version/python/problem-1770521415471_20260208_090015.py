# Last updated: 2/8/2026, 9:00:15 AM
1class Solution:
2    def countSubarrays(self, nums: List[int], k: int) -> int:
3        maxx = deque()
4        minn = deque()
5        l = 0
6        count = 0
7        for r in range(len(nums)):
8            while maxx and nums[maxx[-1]]<nums[r]:
9                maxx.pop()
10            maxx.append(r)
11
12            while minn and nums[minn[-1]]>nums[r]:
13                minn.pop()
14            minn.append(r)
15
16            while(nums[maxx[0]]-nums[minn[0]])*(r-l+1)>k:
17                if maxx[0] == l:
18                    maxx.popleft()
19                if minn[0] == l:
20                    minn.popleft()
21                l+=1
22            count+=(r-l+1)
23        return count