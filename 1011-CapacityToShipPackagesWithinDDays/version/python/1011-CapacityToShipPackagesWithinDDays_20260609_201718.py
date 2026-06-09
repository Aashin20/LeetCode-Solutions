# Last updated: 6/9/2026, 8:17:18 PM
1class Solution:
2    def shipWithinDays(self, weights: List[int], days: int) -> int:
3        def can_ship(k):
4            days_used = 1
5            cur = 0
6
7            for w in weights:
8                if cur + w > k:
9                    days_used += 1
10                    cur = w
11                else:
12                    cur += w
13
14            return days_used <= days
15        L=max(weights)
16        R=sum(weights)
17        while L<R:
18            k=(L+R)//2
19            if can_ship(k):
20                R=k
21            else:
22                L=k+1
23        return L
24            