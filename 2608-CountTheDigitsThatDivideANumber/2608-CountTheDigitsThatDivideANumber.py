# Last updated: 6/14/2025, 10:32:09 PM
from collections import defaultdict

class Solution:
    def countDigits(self, num):
        num_str = str(num)
        digits = [int(d) for d in list(num_str)]
        digit_to_freq_map = defaultdict(int)
        for digit in digits:
            digit_to_freq_map[digit] += 1
        
        ret_val = 0
        for digit, freq in digit_to_freq_map.items():
            ret_val += freq if (num % digit == 0) else 0

        return ret_val