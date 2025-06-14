# Last updated: 6/14/2025, 10:31:50 PM
class Solution:
    def maxDfromAtoB(self, a: int, b: int, k: int, n: int, freq: List[List[int]]) -> int:
        cnt = float('-inf')
        MOD = 10 ** 8
        minFreq = [[MOD, MOD], [MOD, MOD]]
        freqA = 0
        freqB = 0
        prevA = 0
        prevB = 0
        l = 0
        for r in range(k - 1, n):
            freqA = freq[a][r + 1]
            freqB = freq[b][r + 1]
            while r - l + 1 >= k and freqB - prevB >= 2:
                minFreq[prevA & 1][prevB & 1] = min(minFreq[prevA & 1][prevB & 1], prevA - prevB)
                prevA = freq[a][l + 1]
                prevB = freq[b][l + 1]
                l += 1
            cnt = max(cnt, freqA - freqB - minFreq[1 - (freqA & 1)][freqB & 1])
        return cnt
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        freq = [[0] * (n + 1) for _ in range(5)]
        conter = Counter(s)
        for i in range(n):
            for d in range(5):
                freq[d][i + 1] = freq[d][i]
            freq[int(s[i])][i + 1] += 1
        ans = float('-inf')
        for a in range(5):
            if freq[a][n] == 0:
                continue
            for b in range(5):
                if a == b or freq[b][n] == 0:
                    continue
                ans = max(ans, self.maxDfromAtoB(a, b, k, n, freq))
        return ans

        