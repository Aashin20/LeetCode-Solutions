# Last updated: 5/7/2026, 11:18:08 PM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        ROW = len(board)
7        COL = len(board[0])
8        def capture(r,c):
9            if (r<0 or r==ROW or c<0 or c==COL or board[r][c]!="O"):
10                return
11            board[r][c]='T'
12            capture(r+1,c)
13            capture(r-1,c)
14            capture(r,c+1)
15            capture(r,c-1)
16        for r in range(ROW):
17            for c in range(COL):
18                if board[r][c]=='O' and (r in [0,ROW-1] or c in [0,COL-1]):
19                    capture(r,c)
20        
21        for r in range(ROW):
22            for c in range(COL):
23                if board[r][c]=='O':
24                    board[r][c]='X'
25        for r in range(ROW):
26            for c in range(COL):
27                if board[r][c]=='T':
28                    board[r][c]='O'