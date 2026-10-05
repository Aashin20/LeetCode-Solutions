# Last updated: 10/5/2026, 10:56:27 PM
1class Solution:
2    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
3        M = len(matrix)
4        N = len(matrix[0])
5        T = M*N
6        L=0
7        R=T-1
8        while L<=R:
9            mid = (L+R)//2
10            i = mid//N
11            j = mid%N
12            val = matrix[i][j]
13            if val==target:
14                return True
15            elif val>=target:
16                R=mid-1
17            else:
18                L=mid+1
19        return False