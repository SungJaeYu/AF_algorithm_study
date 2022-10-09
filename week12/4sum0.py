from sys import stdin

def input_data():
    n = int(stdin.readline().rstrip())
    abcd = []
    for _ in range(n):
        row = list(map(int, stdin.readline().split()))
        abcd.append(row)
    return n, abcd

def main():
    count = 0
    n, abcd = input_data()
    ab_sum = dict()
    for i in range(n):
        for j in range(n):
            ab = abcd[i][0] + abcd[j][1]
            if ab in ab_sum:
                ab_sum[ab] += 1
            else:
                ab_sum[ab] = 1

    for i in range(n):
        for j in range(n):
            cd = abcd[i][2] + abcd[j][3]
            if -cd in ab_sum:
                count += ab_sum[-cd]
    print(count)

main()
