# Last updated: 8/20/2026, 11:26:24 PM
1class Solution:
2    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
3        visited = set()
4        visited.add(0)
5        def visit(room):
6            for i in rooms[room]:
7                if i in visited: 
8                    continue
9                visited.add(i)
10                visit(i)
11        visit(0)
12        return len(visited) == len(rooms)