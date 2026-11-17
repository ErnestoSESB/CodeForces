n, a, b, c = map(int, input().split())
NEG = -10**9
dp = [NEG] * (n + 1)
dp[0] = 0
for x in range(1, n + 1):
    for p in (a, b, c):
        if x >= p and dp[x - p] != NEG:
            dp[x] = max(dp[x], dp[x - p] + 1)
print(dp[n])