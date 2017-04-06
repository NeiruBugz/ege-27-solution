aMax = 10000
n = 6
s = 0
d = aMax - 1

for i in range(1, n + 1):
    a = int(input('>'))
    b = int(input('>'))
    maxim = max(a, b)
    minim = min(a, b)
    s += maxim
    if ((maxim - minim) % 3 != 0) and (maxim - minim < d):
        d = maxim - minim

if s % 3 == 0:
    s = 0 if d > aMax else (s - d)
print(s)