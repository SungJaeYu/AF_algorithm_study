import sys

t = int(input())
for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    if n % h == 0:
        output = h * 100 + (n // h)
    else:
        output = (n % h) * 100 + (n // h + 1)
    print(output)
