n = int(input())
for i in range(1, n + 1):
    k = 2 * i - 1
    for j in range(0, n - i):
        print(" ", end='')
    for j in range(0, k):
        print("*", end='')
    print("\n", end='')
    
for i in range(n-1, 0, -1):
    k = 2 * i - 1
    for j in range(0, n - i):
        print(" ", end='')
    for j in range(0, k):
        print("*", end='')
    if i != 1:
        print("\n", end='')

