# Last updated: 7/23/2026, 12:11:24 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        s=set(nums)
4        longest=0
5        for num in s:
6            if num-1 not in s:
7                length = 1
8                next_num=num+1
9                while next_num in s:
10                    length+=1
11                    next_num+=1
12                longest=max(longest,length)
13        return longest