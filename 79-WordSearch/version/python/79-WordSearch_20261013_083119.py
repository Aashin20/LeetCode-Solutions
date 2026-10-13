# Last updated: 10/13/2026, 8:31:19 AM
1class Solution:
2    def exist(self, board: list[list[str]], word: str) -> bool:
3        m=len(board)
4        n=len(board[0])
5        w=len(word)
6        if m==1 and n==1:
7            return board[0][0]==word
8        def backtrack(pos,index):
9            if index==w:
10                return True
11            i,j=pos
12            if board[i][j]!=word[index]:
13                return False
14            char=board[i][j]
15            board[i][j]='#'
16            for dir_i,dir_j in [(1,0),(0,1),(-1,0),(0,-1)]:
17                r,c=i+dir_i,j+dir_j
18                if 0<=r<m and 0<=c<n:
19                    if backtrack((r,c),index+1):
20                        return True
21            board[i][j]=char
22            return False
23        for i in range(m):
24            for j in range(n):
25                if backtrack((i,j),0):
26                    return True
27        return False