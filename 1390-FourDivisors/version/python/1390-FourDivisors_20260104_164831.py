# Last updated: 1/4/2026, 4:48:31 PM
1class Solution:
2    def sumFourDivisors(self, nums: List[int]) -> int:
3        sum = 0
4        for num in nums:
5            count = 0
6            total = 0
7            for i in range(1, int(num**0.5) + 1):
8                if num % i == 0:
9                    j = num // i
10
11                    if i == j:          # perfect square
12                        count += 1
13                        total += i
14                    else:               # divisor pair
15                        count += 2
16                        total += i + j
17
18                    
19            if count == 4:
20                sum+=total
21            else:
22                continue
23        return sum