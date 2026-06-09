# Last updated: 6/9/2026, 8:04:05 PM
1class Solution:
2    def minEatingSpeed(self, piles: List[int], h: int) -> int:
3        def k_works(k):
4            hours=0
5            for p in piles:
6                hours+=ceil(p/k)
7                if hours>h:
8                    return False
9            return True
10        L=1
11        R=max(piles)
12        while L<R:
13            k=(L+R)//2
14            if k_works(k):
15                R=k
16            else:
17                L=k+1
18        return L
19        