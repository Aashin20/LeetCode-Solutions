# Last updated: 9/19/2026, 10:41:34 PM
1class Solution:
2    def splitArray(self, nums: list[int], k: int) -> int:
3        def canSplit(largest):
4            subarray = 0
5            cur = 0
6            for n in nums:
7                cur+=n
8                if cur>largest:
9                    subarray+=1
10                    cur=n
11            return subarray+1<=k
12        L=max(nums)
13        R=sum(nums)
14        while L<=R:
15            M=(L+R)//2
16            if canSplit(M):
17                R=M-1
18            else:
19                L=M+1
20        return L