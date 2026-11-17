n = int(input())
a = list(map(int, input().split()))
total = sum(a)
melhor = 0
for i in range(n):
    for j in range(i, n):
        ganho = 0
        for k in range(i, j + 1):
            ganho += 1 if a[k] == 0 else -1
        melhor = max(melhor, ganho)
if total == n:
    print(n - 1)
else:
    print(total + melhor)