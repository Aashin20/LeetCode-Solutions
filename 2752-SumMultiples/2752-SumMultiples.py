# Last updated: 6/14/2025, 10:32:03 PM
class Solution:
    def sum_of_k_consecutive_multiples_of_x(self, x, k):
        return x * k * (k+1) // 2

    def sumOfMultiples(self, n: int) -> int:
        no_div_by_3 = n // 3
        no_div_by_5 = n // 5
        no_div_by_7 = n // 7

        no_div_by_15 = n // 15
        no_div_by_35 = n // 35
        no_div_by_21 = n // 21

        no_div_by_105 = n // 105

        sum = self.sum_of_k_consecutive_multiples_of_x(3, no_div_by_3) + self.sum_of_k_consecutive_multiples_of_x(5, no_div_by_5) + self.sum_of_k_consecutive_multiples_of_x(7, no_div_by_7) - self.sum_of_k_consecutive_multiples_of_x(15, no_div_by_15) - self.sum_of_k_consecutive_multiples_of_x(35, no_div_by_35) - self.sum_of_k_consecutive_multiples_of_x(21, no_div_by_21) + self.sum_of_k_consecutive_multiples_of_x(105, no_div_by_105)

        return int(sum)