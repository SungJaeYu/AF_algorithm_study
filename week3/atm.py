import sys

# 입력
num_people = int(sys.stdin.readline().rstrip("\n"))
list_people_time = list(map(int, sys.stdin.readline().split()))

# 가장 시간이 적은 사람부터 greedy하게 선택해야되므로 sort
# But, 시간 합을 순차적으로 구하기 위해 내림차순으로 sort(reverse)
list_people_time.sort(reverse=True)

output_time = 0

# 가장 큰 사람은 1번 더해지고, 두번째는 2번 더해진다. 
# 결국 가장 빠른 사람은 n 번 곱해져서 더해진다.
# 이를 활용하여 시간의 전체 합 계산
for i, time in enumerate(list_people_time):
    output_time += (i + 1) * int(time)
    
print(output_time)
