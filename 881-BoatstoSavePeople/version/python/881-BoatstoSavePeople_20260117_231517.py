# Last updated: 1/17/2026, 11:15:17 PM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        L=0
5        R=len(people)-1
6        boats = 0
7        while L<=R:
8            weight = limit-people[R]
9            R-=1
10            boats+=1
11            if L<=R and weight>=people[L]:
12                L+=1
13        return boats