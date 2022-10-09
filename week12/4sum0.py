from sys import stdin

def input_data():
    n = int(stdin.readline().rstrip())
    abcd = []
    for _ in range(n):
        row = list(map(int, stdin.readline().split()))
        abcd.append(row)
    return n, abcd

def sum_two_list(n, abcd):
    ab_sum = []
    cd_sum = []
    for i in range(n):
        for j in range(n):
            ab_sum.append(abcd[i][0] + abcd[j][1])
            cd_sum.append(abcd[i][2] + abcd[j][3])

    return ab_sum, cd_sum

def main():
    count = 0
    n, abcd = input_data()
    ab_sum, cd_sum = sum_two_list(n, abcd)
    sorted_ab_sum = sorted(ab_sum)
    sorted_cd_sum = sorted(cd_sum)
    bound = 0
    length_of_sum = n * n
    for ab in sorted_ab_sum:
        for i in range(bound, length_of_sum):
            if -ab == sorted_cd_sum[length_of_sum - i - 1]:
                count += 1
                bound = i
                break;
    print(count)

main()
