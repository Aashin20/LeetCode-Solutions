# Last updated: 5/30/2026, 8:30:37 PM
1from collections import deque
2class Solution:
3    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
4        p_que = deque()
5        p_seen = set()
6
7        a_que = deque()
8        a_seen = set()
9
10        ROWS,COLS = len(heights), len(heights[0])
11
12        for j in range(COLS):
13            p_que.append((0,j))
14            p_seen.add((0,j))
15        
16        for i in range(1,ROWS):
17            p_que.append((i,0))
18            p_seen.add((i,0))
19        
20        for j in range(ROWS):
21            a_que.append((j,COLS-1))
22            a_seen.add((j,COLS-1))
23        
24        for i in range(COLS-1):
25            a_que.append((ROWS-1,i))
26            a_seen.add((ROWS-1,i))
27
28        def coords(q,seen):
29            while q:
30                i,j = q.popleft()
31                for dirR,dirL in [(0,1),(1,0),(-1,0),(0,-1)]:
32                    r,c = i+dirR,j+dirL
33                    if 0<=r<ROWS and 0<=c<COLS and heights[i][j]<=heights[r][c] and (r,c) not in seen:
34                        seen.add((r,c))
35                        q.append((r,c))
36            return seen
37        
38        p_coords=coords(p_que,p_seen)
39        a_coords=coords(a_que,a_seen)
40        return list(p_coords.intersection(a_coords))