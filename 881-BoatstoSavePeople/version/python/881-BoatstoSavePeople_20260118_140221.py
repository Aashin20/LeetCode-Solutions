# Last updated: 1/18/2026, 2:02:21 PM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        l, r = 0, len(people) - 1
5        boats = 0
6        while l <= r:
7            if people[l] + people[r] <= limit:
8                l += 1
9            r -= 1
10            boats += 1
11        return boats