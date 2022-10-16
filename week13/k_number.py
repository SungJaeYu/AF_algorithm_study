from sys import stdin

N = int(stdin.readline())
k = int(stdin.readline())
left = 1
right = k

while left < right:
    sum = 0
    mid = (left + right) // 2
    for i in range(1, N+1):
        if mid // i == 0:
            break;
        sum += min(mid // i, N)
  
    if sum < k:
        left = mid + 1
    else:
        right = mid

print(left)
