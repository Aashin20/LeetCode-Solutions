# Last updated: 4/2/2026, 11:22:50 PM
1class Solution:
2  def convert(self, s: str, numRows: int) -> str:
3    rows = [''] * numRows
4    k = 0
5    direction = (numRows == 1) - 1
6    for c in s:
7      rows[k] += c
8      if k == 0 or k == numRows - 1:
9        direction *= -1
10      k += direction
11    return ''.join(rows)