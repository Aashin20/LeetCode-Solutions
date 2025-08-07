# Last updated: 8/8/2025, 12:08:05 AM
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        total = sum(fruits[i][i] for i in range(n))

        right_path = [0] * 3
        right_path[0] = fruits[0][n - 1]

        bottom_path = [0] * 3
        bottom_path[0] = fruits[n - 1][0]

        window = 2

        for step in range(1, n - 1):
            new_right = [0] * (window + 2)
            new_bottom = [0] * (window + 2)

            for dist in range(window):
                left = right_path[dist - 1] if dist - 1 >= 0 else 0
                mid = right_path[dist]
                right = right_path[dist + 1] if dist + 1 < len(right_path) else 0
                new_right[dist] = max(left, mid, right) + fruits[step][n - 1 - dist]

                left = bottom_path[dist - 1] if dist - 1 >= 0 else 0
                mid = bottom_path[dist]
                right = bottom_path[dist + 1] if dist + 1 < len(bottom_path) else 0
                new_bottom[dist] = max(left, mid, right) + fruits[n - 1 - dist][step]

            right_path = new_right
            bottom_path = new_bottom

            if window - n + 4 + step <= 1:
                window += 1
            elif window - n + 3 + step > 1:
                window -= 1

        return total + right_path[0] + bottom_path[0]
