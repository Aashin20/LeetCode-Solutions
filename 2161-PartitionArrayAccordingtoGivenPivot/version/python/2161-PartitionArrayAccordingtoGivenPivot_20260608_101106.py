# Last updated: 6/8/2026, 10:11:06 AM
1class Solution:
2    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
3        small=[]
4        great=[]
5        count=0
6        for i in nums:
7            if i<pivot:
8                small.append(i)
9            elif i>pivot:
10                great.append(i)
11            else: count+=1
12        equal=[pivot]*count
13        return small+equal+great
14