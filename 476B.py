s1 = input().strip()
s2 = input().strip()
alvo = s1.count('+') - s1.count('-')
pos = s2.count('+') - s2.count('-')
q = s2.count('?')
total = 1 << q
ok = 0
for mask in range(total):
    p = pos
    for i in range(q):
        p += 1 if (mask >> i) & 1 else -1
    if p == alvo:
        ok += 1
print("%.12f" % (ok / total))