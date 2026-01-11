# Last updated: 1/11/2026, 11:02:26 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        L = 0
4        R = len(numbers)-1
5        while L<R:
6            addition = numbers[L]+numbers[R]
7            if addition == target:
8                return [L+1,R+1]
9            elif addition<target:
10                L+=1
11            else:
12                R-=1