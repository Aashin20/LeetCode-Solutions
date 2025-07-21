# Last updated: 7/21/2025, 10:33:30 PM
class Solution:
    def makeFancyString(self, s: str) -> str:
        result = s[0]
        last = s[0]
        count = 1

        for i in range(1, len(s)):
            if s[i] != last:
                last = s[i]
                count = 0

            count += 1
            if count > 2:
                continue

            result += s[i]

        return result
