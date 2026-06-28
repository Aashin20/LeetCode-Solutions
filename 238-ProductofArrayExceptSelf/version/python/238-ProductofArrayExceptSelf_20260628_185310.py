# Last updated: 6/28/2026, 6:53:10 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        prefix = defaultdict(int)
4        prefix[0] = 1 
5        count=0
6        sum=0
7        for num in nums:
8            sum+=num
9            if (sum-k) in prefix:
10                count+=prefix[sum-k]
11            prefix[sum]+=1
12
13        return count
14        