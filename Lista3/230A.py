s, n = map(int, input().split())
dragoes = []
for _ in range(n):
    x, y = map(int, input().split())
    dragoes.append((x, y))
dragoes.sort()
ok = True
for x, y in dragoes:
    if s > x:
        s += y
    else:
        ok = False
        break
print("YES" if ok else "NO")
