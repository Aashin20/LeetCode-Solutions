# Last updated: 1/17/2026, 11:10:00 PM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        L=0
5        R=len(people)-1
6        boats = 0
7        while L<=R:
8            weight = people[L]+people[R]
9            if weight<=limit:
10                boats+=1
11                L+=1
12                R-=1
13            else:
14                boats+=1
15                if people[L]>people[R]:
16                    L+=1
17                else:
18                    R-=1
19        return boats
20            