n = int(input())
a = list(map(int, input().split()))
M = 100001
cnt = [0] * (M + 1)
for x in a:
    cnt[x] += 1
dp = [0] * (M + 1)
dp[1] = cnt[1]
for v in range(2, M + 1):
    dp[v] = max(dp[v - 1], dp[v - 2] + v * cnt[v])
print(dp[M])