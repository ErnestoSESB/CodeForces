n, k = map(int, input().split())
a = sorted(map(int, input().split()))
meio = n // 2
def pode(x):
    custo = 0
    for i in range(meio, n):
        if a[i] < x:
            custo += x - a[i]
        if custo > k:
            return False
    return custo <= k
lo, hi = a[meio], a[meio] + k
while lo < hi:
    mid = (lo + hi + 1) // 2
    if pode(mid):
        lo = mid
    else:
        hi = mid - 1
print(lo)