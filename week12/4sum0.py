from sys import stdin

def input_data():
    n = int(stdin.readline().rstrip())
    abcd = []
    for _ in range(n):
        row = list(map(int, stdin.readline().split()))
        abcd.append(row)
    return n, abcd

def sum_two_list(n, abcd):
    ab_sum = dict()
    cd_sum = dict()
    for i in range(n):
        for j in range(n):
            ab = abcd[i][0] + abcd[j][1]
            cd = abcd[i][2] + abcd[j][3]
            if ab in ab_sum:
                ab_sum[ab] += 1
            else:
                ab_sum[ab] = 1

            if cd in cd_sum:
                cd_sum[cd] += 1
            else:
                cd_sum[cd] = 1

    return ab_sum, cd_sum

def main():
    result = 0
    n, abcd = input_data()
    ab_sum, cd_sum = sum_two_list(n, abcd)
    bound = 0
    for ab, count in ab_sum.items():
        if -ab in cd_sum:
            result += count * cd_sum[-ab] 
    
    print(result)

main()
