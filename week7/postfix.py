import sys

OPERATOR = ['+', '-', '*', '/']
BRACKET = ['(', ')']
stack = []
output = []
def main():
    calculation = [*sys.stdin.readline().strip()]
    for c in calculation:
        if c in OPERATOR:
           stack.append(c)
        elif c in BRACKET:
            pass
        else:
            output.append(c)
    if len(stack) != 0:
        while len(stack) != 0:
            output.append(stack.pop())
    for c in output:
        print(c, end='')

main()
