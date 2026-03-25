# Last updated: 3/25/2026, 10:23:48 PM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        ROW = len(board)
7        COL = len(board[0])
8        #Change O in edge to T
9        def capture(r,c):
10            if (r<0 or c<0 or r==ROW or c==COL or board[r][c]!='O'):
11                return
12            board[r][c]='T'
13            capture(r+1,c)
14            capture(r-1,c)
15            capture(r,c+1)
16            capture(r,c-1)
17        #Change Os to T
18        for r in range(ROW):
19            for c in range(COL):
20                if board[r][c]=='O' and (r in [0,ROW-1] or (c in [0,COL-1])):
21                    capture(r,c)
22        for r in range(ROW):
23            for c in range(COL):
24                if board[r][c]=='O':
25                    board[r][c]='X'
26        #Change Ts to X
27        for r in range(ROW):
28            for c in range(COL):
29                if board[r][c]=='T':
30                    board[r][c]='O'