# Last updated: 1/1/2026, 11:10:56 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        for i in reversed(range(len(digits))):
4            if digits[i] == 9:
5                digits[i] = 0
6            else:
7                digits[i] += 1
8                return digits
9        return [1] + digits
10        