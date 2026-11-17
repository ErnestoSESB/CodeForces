n = int(input())
a = sorted(map(int, input().split()), reverse=True)
total = sum(a)
minha = 0
cont = 0
for x in a:
    minha += x
    cont += 1
    if minha > total - minha:
        break
print(cont)