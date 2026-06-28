# Last updated: 6/28/2026, 7:13:18 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        prefix=defaultdict(int)
4        prefix[0]=1
5        summ=0
6        count=0
7        for num in nums:
8            summ+=num
9            if (summ-k) in prefix:
10                count+=prefix[summ-k]
11            prefix[summ]+=1
12        return count