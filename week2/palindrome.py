import sys

def is_palindrome_not_check_pseudo(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue
        temp1 = s[left + 1 : right + 1]
        temp2 = s[left : right]
        if is_palindrome_not_check_pseudo(temp1) or is_palindrome_not_check_pseudo(temp2):
            return 1
        else:
            return 2 
    return 0

num = int(sys.stdin.readline().rstrip("\n"))
for _ in range(num):
    s = sys.stdin.readline().rstrip("\n")
    output = is_palindrome(s)
    print(output)
